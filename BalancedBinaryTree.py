class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class FindDepth:
    @staticmethod
    def maxdepth(root):
        if root is None:
            return 0
        leftdepth = FindDepth.maxdepth(root.left)
        rightdepth = FindDepth.maxdepth(root.right)
        if leftdepth == -1 or rightdepth == -1:
            return -1
        if abs(leftdepth-rightdepth)>1:
            return -1
        return 1+max(leftdepth,rightdepth)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.left.left = Node(7)


# Calculate the maximum depth
fd = FindDepth()
depth = fd.maxdepth(root)

print("Maximum depth of the binary tree:", depth)
