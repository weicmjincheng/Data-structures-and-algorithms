# _*_coding:utf-8 _*_
"""
@Time    :2018/7/8 16:39
@Author  :weicm
#@Software: PyCharm
# 二分查找 操作有序的序列 时间复杂度 O（logn）  最优时间复杂度是O(1)
"""


# 递归版本
def binary_search(alist,item):
    n = len(alist)
    # 递归停止条件
    if n > 0 :
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    else:
        print("您查找的元素不存在")
        return False


# 非递归版本
def binary_search2(alist, item):
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last) //2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == "__main__":
    # 查找的是有序集合
    li = [17, 22, 30, 44, 52, 63, 71, 80]
    search_result = binary_search2(li, 100)
    print(search_result)
