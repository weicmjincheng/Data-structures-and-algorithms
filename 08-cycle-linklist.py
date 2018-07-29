# _*_coding:utf-8 _*_
"""
@Time    :2018/7/7 16:04
@Author  :weicm
#@Software: PyCharm
"""


# 定义节点
class Node(object):
    def __init__(self,item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    # 设置默认参数
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        # 定义一个游标，然后从头向后走
        cur = self.__head
        # count记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 定义一个游标，然后从头向后走
        cur = self.__head
        while cur is not None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        # 头节点插入 构造节点  头插法
        node = Node(item)
        # 定义一个游标，然后从头向后走
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        # 构造节点 尾节点插入  尾插法
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            # 定义一个游标，然后从头向后走
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        # pos 起始从零开始
        # 定义一个游标，然后从头向后走
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos :
                count += 1
                cur = cur.next
            node = Node(item)
            # 当循环退出后指针指向pos - 1位置
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node


    def remove(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                # 先判断是否是头节点
                if cur == self.__head:
                    self.__head == cur.next
                    # 判断节点是否为一个的情况
                    if cur.next:
                        cur.next.prev = cur.prev
                else:
                    # 包含了为节点的情况
                    cur.prev.next = cur.next
                    # 判断当为最后一个节点的情况
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        cur = self.__head
        count = 0
        while cur.elem != item:
            count += 1
            cur = cur.next
        return count


if __name__ == "__main__":
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.insert(2,100)
    # Ll.insert(0, 5)
    dll.travel()
    print(dll.search(5))
    print("="*20)
    dll.remove(2)
    dll.travel()