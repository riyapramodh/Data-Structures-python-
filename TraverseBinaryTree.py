class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def add(self):
        root = Node(1)
        root.left  = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        return root
    def preorder(self,node):
        if node is None:
            return
        else:
            print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)


    def print(self,node):
        if node is None:
            return
        else:
            print(node.data)
        self.print(node.left)
        self.print(node.right)

bt = BinaryTree()
node = bt.add()
bt.print(node)
print("------------------------------------------------------------------------------------------------")
bt.preorder(node)
print("-------------------------------------------------------------------------------------------------")
bt.inorder(node)
print("-------------------------------------------------------------------------------------------------")
bt.postorder(node)








