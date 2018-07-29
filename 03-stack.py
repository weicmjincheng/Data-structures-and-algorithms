# _*_coding:utf-8 _*_
"""
@Time    :2018/7/2 8:52
@Author  :weicm
#@Software: PyCharm
# 栈的实现  Stack() 创建一个空栈    push(item) 压栈   pop() 弹栈    peek() 返回栈顶端元素  元素不出栈（查询）
            is_empty() 判断栈是否为空    size() 返回栈的元素个数
"""


class Stack(object):
    # 栈
    def __init__(self):
        self.__list = []

    def push(self,item):
        # 从尾部添加取的时候也是从尾部取 时间复杂度O(1)
        self.__list.append(item)
        # 从头部添加取的时候也从头部取出 O(n)
        # self.__list.insert(0,item)

    def pop(self):
        # 从尾部取元素 O(1)
        return self.__list.pop()
        # 头部取出元素 O(n)
        # self.__list.pop(0)

    def peek(self):
        if self.__list:
            return self.__list(-1)
        else:
            return None

    def is_empty(self):
        return self.__list == []
        # return not self.__list

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

"""
5
4
3
2
1
"""