from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Binarytree:
    def add(self):
        data = int(input())
        if data == -1:
            return None
        root = Node(data)
        q = deque()
        q.append(root)

        node = q.popleft()
        leftdata = int(input())
        if leftdata == -1:
            return None
        left = Node(leftdata)
        node.left = left
        q.append(left)

        rightdata = int(input())
        if rightdata == -1:
            return None
        right = Node(rightdata)
        node.right = right
        q.append(right)

        return root

    def levelordertraversal(self,node):
        if node is None:
            return None
        q = deque()
        q.qppend(node)

        while q is True:
            node = q.popleft()
            print(node.data)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
bt = Binarytree
temp = bt
flag = bt.levelordertraversal(temp)

