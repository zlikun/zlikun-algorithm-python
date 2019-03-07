#!/usr/bin/env python
# -- coding: utf-8 --
"""
@AUTHOR : zlikun <zlikun-dev@hotmail.com>
@DATE   : 2019/03/07 10:08:49
@DESC   : 冒泡排序进阶二：除了在轮数上减少，还可以在每轮比较次数上减少
"""

numbers = [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]


def bubble_sort(lst: "list"):
    length = len(lst)
    # 初始有序边界最后一个索引位置（即：没有有序序列）
    border = length - 1
    for i in range(length - 1):
        # 设定一个有序标记，假定初始有序，后续遍历过程中一旦发生交换，则表示无序，未发生交换，表示序列有序
        flag = True
        # 每轮比较设置一个最后有序索引，每次比较更新该索引，直到该轮结束，该索引之后的元素未发生比较，其后序列为有序序列
        last_index = -1
        # 因为每轮都是从无序序列中找到最大值，将其移动到有序位置，那么该位置就是有序边界，其右为有序序列，其左为无序序列
        for j in range(border):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                flag = False
                last_index = j
        # 一轮比较结束后，更新有序边界
        border = last_index
        if flag:
            break


if __name__ == '__main__':
    # 排序前： [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]
    print('排序前：', numbers)
    # 执行排序
    bubble_sort(numbers)
    # 排序后： [8, 8, 32, 142, 153, 221, 231, 235, 244, 248]
    print('排序后：', numbers)
