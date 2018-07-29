# _*_coding:utf-8 _*_
"""
@Time    :2018/7/2 17:02
@Author  :weicm
#@Software: PyCharm
# 单向链表  is_empty() 判断是否为空   length() 链表长度   travel() 遍历整个链表    add(item)  链表头部添加元素
        append(item) 链表尾部添加元素  insert(pos,item) 制定位置添加元素   remove(item) 删除节点  search(item) 查找结点是否存在
"""

class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    # 设置默认参数
    def __init__(self,node=None):
        self.__head = node

    def is_empty(self):
        return  self.__head == None

    def length(self):
        # 定义一个游标，然后从头向后走
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count+=1
            cur = cur.next
        return count

    def travel(self):
        # 定义一个游标，然后从头向后走
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self,item):
        # 头节点插入 构造节点  头插法
        node = Node(item)
        # 定义一个游标，然后从头向后走
        node.next = self.__head
        self.__head = node


    def append(self,item):
        # 构造节点 尾节点插入  尾插法
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            # 定义一个游标，然后从头向后走
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        # pos 起始从零开始
        # 定义一个游标，然后从头向后走
        """
        # 自己写的方法 根据指针和统计个数来确定
        cur = self.__head
        node = Node(item)
        count = 0
        while cur != None and count !=pos - 1 :
            count += 1
            cur = cur.next
        node.next = cur.next
        cur.next = node

        """
        if pos <= 0 :
            Ll.add(item)
        elif pos > Ll.length()-1:
            Ll.append(item)
        else:
            node = Node(item)
            # 方法二：定义pre指针
            pre = self.__head
            count = 0
            while pre != None and count != pos - 1:
                count += 1
                pre = pre.next
            # 当循环退出后指针指向pos - 1位置
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        """
        # 自己做的有问题没有考虑特殊情况 需要补充头和尾两种特殊情况
        i = Ll.search(item)
        cur = self.__head
        count = 0
        while count != i - 1:
            count += 1
            cur = cur.next
        cur.next = cur.next.next
        """
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem ==item:
                # 先判断是否是头节点
                if cur == self.__head:
                    self.__head == cur.next
                else:
                    # 包含了为节点的情况
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
        cur = self.__head
        count = 0
        while cur.elem!=item:
            count+=1
            cur = cur.next
        return count
    """
    方法二：
    cur = self.__head
    while cur!=None:
        if cur.elem == item:
            return Ture
        else:
            cur = cur.next
    return False
    """


if __name__ == "__main__":
    Ll = SingleLinkList()
    print(Ll.is_empty())
    # print(Ll.length())
    Ll.append(1)
    Ll.append(2)
    Ll.append(3)
    Ll.append(4)
    Ll.append(5)
    Ll.insert(2,100)
    # Ll.insert(0, 5)
    Ll.travel()
    print(Ll.search(5))
    print("="*20)
    Ll.remove(2)
    Ll.travel()

