#!/usr/bin/env python
# -- coding: utf-8 --
"""
@AUTHOR : zlikun <zlikun-dev@hotmail.com>
@DATE   : 2019/03/12 19:23:03
@DESC   : 希尔排序
"""

numbers = [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]


def shell_sort(lst: "list"):
    gap = len(lst) // 2
    while gap > 0:
        # 从1开始遍历
        for i in range(gap, len(lst), gap):
            # 左边反向遍历
            sentinel = lst[i]
            # 内层循环写法一
            j = i - gap
            while j > 0 and sentinel < lst[j]:
                lst[j + gap], lst[j] = lst[j], sentinel
                j -= gap
            # # 内层循环写法二
            # for j in range(i - gap, -1, -gap):
            #     if sentinel < lst[j]:
            #         lst[j + gap], lst[j] = lst[j], sentinel
            #     else:
            #         break
        gap //= 2


if __name__ == '__main__':
    # 排序前： [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]
    print('排序前：', numbers)
    # 执行排序
    shell_sort(numbers)
    # 排序后： [8, 8, 32, 142, 153, 221, 231, 235, 244, 248]
    print('排序后：', numbers)
