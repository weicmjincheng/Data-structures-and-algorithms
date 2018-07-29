# _*_coding:utf-8 _*_
"""
@Time    :2018/7/2 15:56
@Author  :weicm
#@Software: PyCharm
# 双端队列  Deque() 创建空的双端队列    add_front(item) 从队头添加元素   add_rear(item) 从队尾添加元素
            remove_front() 从队头删除元素   remove_rear() 从队尾删除元素   is_empty() 判断双端队列是否为空
            size() 返回队列大小
"""


class Dequeue(object):
    def __init__(self):
        self.__list = []

    def add_front(self,item):
        return self.__list.insert(0,item)

    def add_rear(self,item):
        return self.__list.append(item)

    def remove_front(self):
        return self.__list.pop(0)

    def remove_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    q = Dequeue()
    print("=" * 20 + "头部添加与删除" + "=" * 20)
    q.add_front(1)
    q.add_front(2)
    q.add_front(3)
    q.add_front(4)
    q.add_front(5)

    print(q.remove_front())
    print(q.remove_front())
    print(q.remove_front())
    print(q.remove_front())
    print(q.remove_front())
    print("="*20+"尾部添加与删除"+"="*20)
    q.add_rear(1)
    q.add_rear(2)
    q.add_rear(3)
    q.add_rear(4)
    q.add_rear(5)
    # print(q.size())
    print(q.remove_rear())
    print(q.remove_rear())
    print(q.remove_rear())
    print(q.remove_rear())
    print(q.remove_rear())
    # print(q.size())

"""
====================头部添加与删除====================
5
4
3
2
1
====================尾部添加与删除====================
5
4
3
2
1

"""
