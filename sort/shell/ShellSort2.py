#!/usr/bin/env python
# -- coding: utf-8 --
"""
@AUTHOR : zlikun <zlikun-dev@hotmail.com>
@DATE   : 2019/03/12 19:23:03
@DESC   : 希尔排序，就换种写法而已
"""

numbers = [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]


def shell_sort(lst: "list"):
    for gap in gap_generator(len(lst)):
        for i in range(gap, len(lst), gap):
            sentinel = lst[i]
            j = i - gap
            while j > 0 and sentinel < lst[j]:
                lst[j + gap], lst[j] = lst[j], sentinel
                j -= gap


def gap_generator(length):
    """
    缩小增量序列生成器
    :param length:
    :return:
    """
    gap = length // 2
    while gap > 0:
        yield gap
        gap //= 2


if __name__ == '__main__':
    # 排序前： [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]
    print('排序前：', numbers)
    # 执行排序
    shell_sort(numbers)
    # 排序后： [8, 8, 32, 142, 153, 221, 231, 235, 244, 248]
    print('排序后：', numbers)
