# _*_coding:utf-8 _*_
"""
@Time    :2018/7/7 22:18
@Author  : weicm
#@Software: PyCharm
# 希尔排序  时间复杂度O(n^2)   不稳定
"""


def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    # gap变化到0之前，插入算法执行的次数
    while gap > 0:  # 与普通的插入算法区别就是gap的步长
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    # 比较全部
                    i -= gap
                else:
                    break
        # 缩短gap步长
        gap //= 2


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)