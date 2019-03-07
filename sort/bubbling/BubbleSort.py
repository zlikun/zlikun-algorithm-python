#!/usr/bin/env python
# -- coding: utf-8 --
"""
@AUTHOR : zlikun <zlikun-dev@hotmail.com>
@DATE   : 2019/03/07 10:08:49
@DESC   : 冒泡排序
"""

numbers = [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]


def bubble_sort(lst: "list"):
    length = len(lst)
    # 外层控制比较轮数
    for i in range(length - 1):
        # 内层控制每轮比较，大数向右移，移动到有序位置后，右边界收缩
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


if __name__ == '__main__':
    # 排序前： [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]
    print('排序前：', numbers)
    # 执行排序
    bubble_sort(numbers)
    # 排序后： [8, 8, 32, 142, 153, 221, 231, 235, 244, 248]
    print('排序后：', numbers)
