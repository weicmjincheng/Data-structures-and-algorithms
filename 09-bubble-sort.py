# _*_coding:utf-8 _*_
"""
@Time    :2018/7/7 19:24
@Author  :weicm
#@Software: PyCharm
# 冒泡排序法 顺序表实现  最大值向后走   稳定
"""


# 自己做的有的地方需要重新完善 时间复杂度n^2
def bubble_soft(alist):
    # 控制走的总体步数 代表第几次遍历
    for j in range(len(alist)-1):
        # 当给的列表是有序的情况 给定一个计数
        count = 0
        n = len(alist)-1
        for i in range(0, n):
            # 比较相邻两个元素大小 每次产生一个最高元素
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
            n -= 1
        if count == 0:
            return


# 标准做法
def bubble_soft2(alist):
    # 控制走的总体步数 代表第几次遍历
    n = len(alist)
    for j in range(n-1):
        for i in range(0, n-1-j):
            # 比较相邻两个元素大小 每次产生一个最高元素
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_soft(li)
    # bubble_soft2(li)
    print(li)
