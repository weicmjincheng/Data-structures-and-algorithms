# _*_coding:utf-8 _*_
"""
@Time    :2018/7/2 15:26
@Author  :weicm
#@Software: PyCharm
# 队列  队头取出  队尾添加   Queue() 创建空队列    enqueue(item) 往队列添加一个item元素
        dequeue() 从头删除一个元素   is_empty() 判断是否为空   size() 返回队列大小
"""


class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self,item):
        return self.__list.append(item)
        # self.__list.insert(0,item) 从头部添加

    def dequeue(self):
        return self.__list.pop(0)
        # 从尾部弹出 self.__list.pop()  来回变换时间复杂度次相同  看具体使用那个次数多

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

"""
1
2
3
4
5
"""