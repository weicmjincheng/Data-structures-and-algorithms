# _*_coding:utf-8 _*_
"""
@Time    :2018/7/8 8:33
@Author  :weicm
#@Software: PyCharm
# 快速排序  时间复杂度O(n^2)  最有时间复杂度O(nlogn)   不稳定  重要
"""


def quick_sort(alist,first,last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # 让high游标左移  等于表示将相等的元素都放在右边
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        # 让low游标右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 整个循环退出时low与high是相等的
    alist[low] = mid_value
    # 对low左边的执行快速排序
    quick_sort(alist,first,low-1)
    # 对low右边的进行排序
    quick_sort(alist,low+1,last)


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)