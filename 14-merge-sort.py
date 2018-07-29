# _*_coding:utf-8 _*_
"""
@Time    :2018/7/8 14:36
@Author  :weicm
#@Software: PyCharm
# 归并算法 拆分将所有子元素全部分开然后合并
# 时间复杂度 O(nlogn)  稳定  但需要额外空间取接受返回值
"""


def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    # left right 采用排序后形成的新的列表
    left_li = merge_sort(alist[:mid])

    right_li = merge_sort(alist[mid:])

    # 将两个有序的合并成整体
    left_pointer, right_pointer = 0, 0
    # 建新列表用来存放结果值
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    sorted_li = merge_sort(li)
    print(sorted_li)