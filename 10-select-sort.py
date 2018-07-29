# _*_coding:utf-8 _*_
"""
@Time    :2018/7/7 20:17
@Author  :weicm
#@Software: PyCharm
# 选择排序  最小值放到最前面的位置   不稳定
"""


def select_sort(alist):
    n = len(alist)
    # 从0遍历到倒数第二个元素 时间复杂度：O(n^2)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        #  交换下标
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)


