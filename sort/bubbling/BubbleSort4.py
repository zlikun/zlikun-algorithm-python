#!/usr/bin/env python
# -- coding: utf-8 --
"""
@AUTHOR : zlikun <zlikun-dev@hotmail.com>
@DATE   : 2019/03/07 10:08:49
@DESC   : 冒泡排序进阶三：鸡尾酒排序，同时向两边冒泡（小向左，大向右，减少整体比较轮数），
本例是在未优化版本上修改得来，仍可以使用2、3中的方法进一步优化
"""

numbers = [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]


def bubble_sort(lst: "list"):
    """
    鸡尾酒排序
    :param lst: 无序序列
    :return:
    """
    length = len(lst)  # 序列长度
    left = 0  # 左边界
    right = length - 1  # 右边界
    # 轮数由左右边界相遇决定
    while left < right:
        # 小数向左冒泡（注意从后向前遍历）
        for i in range(right, left, -1):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        left += 1
        # 大数向右冒泡
        for i in range(left, right):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        right -= 1


if __name__ == '__main__':
    # 排序前： [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]
    print('排序前：', numbers)
    # 执行排序
    bubble_sort(numbers)
    # 排序后： [8, 8, 32, 142, 153, 221, 231, 235, 244, 248]
    print('排序后：', numbers)
