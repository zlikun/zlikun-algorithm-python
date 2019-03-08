#!/usr/bin/env python
# -- coding: utf-8 --
"""
@AUTHOR : zlikun <zlikun-dev@hotmail.com>
@DATE   : 2019/03/08 10:08:29
@DESC   : 插入排序
"""

numbers = [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]


def insert_sort(lst: "list"):
    # 假设第一个元素本身为有序序列，其后所有元素为无序序列，将无序序列中每个元素依次插入到有序序列正确位置上即实现插入排序
    for i in range(1, len(lst)):
        # 以无序序列第一个元素为哨兵
        sentinel = lst[i]
        for j in range(i - 1, -1, -1):
            if sentinel < lst[j]:
                lst[j + 1], lst[j] = lst[j], sentinel
            else:
                break


if __name__ == '__main__':
    # 排序前： [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]
    print('排序前：', numbers)
    # 执行排序
    insert_sort(numbers)
    # 排序后： [8, 8, 32, 142, 153, 221, 231, 235, 244, 248]
    print('排序后：', numbers)
