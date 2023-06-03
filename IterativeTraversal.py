class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    @staticmethod
    def iterativepreorder(root):
        if root is None :
            return
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            print(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


    @staticmethod
    def iterativeinorder(root):
        if root is None:
            return
        stack = []
        current = root
        while stack:
            while current:
                stack.append(current)
                current.left()

            current = stack.pop()
            print(current.data)

            current = current.right
    @staticmethod
    def iterativepostorder(root):
        if root is None:
            return
        stack1 = []#for traversing
        stack2 = []#for storing the traversed values
        stack1.append(root)

        while stack1:
            node = stack1.pop()
            stack2.append(node)


            if node.left:
                stack1.append(node.left)
            if node.right :
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            print(node.data)
    @staticmethod
    def add():
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        return root


bt = BinaryTree()
node = bt.add()
print("--------------------------------------------------------------------------------------------------------------------------")
bt.iterativepreorder(node)
print("--------------------------------------------------------------------------------------------------------------------------")
bt.iterativeinorder(node)
print("--------------------------------------------------------------------------------------------------------------------------")
bt.iterativepostorder(node)
print("--------------------------------------------------------------------------------------------------------------------------")



