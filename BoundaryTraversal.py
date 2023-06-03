class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printleaves(root):
    if root is not None:
        printleaves(root.left)
        if root.left is None and root.right is None:
            print(root.data)

        printleaves(root.right)

def printleftside(root):
    if root is not None:
        if root.left:
            print(root.data)
            printleftside(root.left)
        elif root.right:
            print(root.data)
            printleftside(root.right)

def printrightside(root):
    if root is not None:
        if root.right:
            printrightside(root.right)
            print(root.data)
        elif root.left:
            printrightside(root.left)
            print(root.data)

def boundarytraversal(root):
    if root is not None:
        print(root.data)

        printleftside(root.left)
        printleaves(root)
        printrightside(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(9)
root.right.left.left = Node(10)


boundarytraversal(root)
