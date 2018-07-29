# _*_coding:utf-8 _*_
"""
@Time    :2018/7/7 21:34
@Author  :weicm
#@Software: PyCharm
# 插入算法  最优时间复杂度是O(n)    时间复杂度O（n^2）  稳定
"""


def insert_sort(alist):
    n = len(alist)
    # 外层循环  代表的是从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1, n):
        # 内层循环的起始值 代表的是执行从右边的无序序列中取出第一个元素即i位置元素，然后插入前面正确的位置
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                # 比较选出的全部元素
                i -= 1
            else:
                # 当遇到小的元素则之前所有元素都比之小
                break


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)
