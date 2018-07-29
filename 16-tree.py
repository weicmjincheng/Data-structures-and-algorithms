# _*_coding:utf-8 _*_
"""
@Time    :2018/7/8 20:24
@Author  :weicm
#@Software: PyCharm
# 树
"""


class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,item):
        # 构造节点
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        # 这里按queue是否为空应该是错误的 经研究发现return在添加后结束整个循环
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    # 广度遍历
    def breath_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    # 深度遍历  先序遍历 中序遍历  后序遍历   都是以根节点命名

    # 前序
    def preorder(self, node):
        if node is None:
            return
        print(node.elem,end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    # 中序
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        self.inorder(node.rchild)

    # 后序
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=" ")



if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breath_travel()
    print("\n")
    tree.preorder(tree.root)


