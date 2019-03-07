#!/usr/bin/env python
# -- coding: utf-8 --
"""
@AUTHOR : zlikun <zlikun-dev@hotmail.com>
@DATE   : 2019/03/07 10:08:49
@DESC   : 冒泡排序进阶一：每轮比较即使列表有序，仍需要完整比较所有轮，存在一定的浪费，针对该特点进行优化
"""

numbers = [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]


def bubble_sort(lst: "list"):
    length = len(lst)
    for i in range(length - 1):
        # 设定一个有序标记，假定初始有序，后续遍历过程中一旦发生交换，则表示无序，未发生交换，表示序列有序
        flag = True
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                flag = False
        if flag:
            break


if __name__ == '__main__':
    # 排序前： [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]
    print('排序前：', numbers)
    # 执行排序
    bubble_sort(numbers)
    # 排序后： [8, 8, 32, 142, 153, 221, 231, 235, 244, 248]
    print('排序后：', numbers)
