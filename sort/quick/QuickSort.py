#!/usr/bin/env python
# -- coding: utf-8 --
"""
@AUTHOR : zlikun <zlikun-dev@hotmail.com>
@DATE   : 2019/03/07 19:52:01
@DESC   : 快速排序，其实现思路是在每轮比较中设置一个支点，将比支点小的元素放在支点左右，
大支点大的元素放在支点右边，然后以支点为界，左右分别递归该过程，直到整体有序
"""

numbers = [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]


def quick_sort(lst: "list"):
    def inner(lst, left, right):

        # 当左边界不小于右边界时，排序结束
        if left >= right:
            return

        # 以左边第一个元素为支点，将小于该支点的元素交换到支点左边，大于等于支点的元素交换到支点的右边
        pivot = lst[left]
        # 定义低位和高位指针，用于分别从左和从右遍历列表，找到需要交换的元素（与支点比较）
        low = left
        high = right

        while low < high:

            # 从右向左遍历，找到小于支点的元素，此时high标记该元素位置
            while low < high and pivot <= lst[high]:
                high -= 1

            # 将high标记的元素赋值给low索引位，low索引位的元素被支点记录，后续支点将向右移动，从而实现小于支点元素交换到支点左边
            lst[low] = lst[high]

            # 从左向右遍历，找到大于等于支点的元素，此时low标记该元素位置
            while low < high and pivot > lst[low]:
                low += 1

            # 将当前low标记的元素（大于等于支点），交换到high空出的位置，交换后low突出，支点将移动到该点上
            lst[high] = lst[low]

        # low此时空出，刚好用于存放支点数据（支点右移）
        lst[low] = pivot

        # 以支点为界，左右两个子序分别递归执行同样逻辑，支点本身有序所以不参与递归
        inner(lst, left, low - 1)
        inner(lst, low + 1, right)

    inner(lst, 0, len(lst) - 1)


if __name__ == '__main__':
    # 排序前： [8, 231, 244, 32, 221, 248, 8, 153, 142, 235]
    print('排序前：', numbers)
    # 执行排序
    quick_sort(numbers)
    # 排序后： [8, 8, 32, 142, 153, 221, 231, 235, 244, 248]
    print('排序后：', numbers)
