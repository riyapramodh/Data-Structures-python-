class Node:
    def __init__ (self,data):
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
        return 1 + max(leftdepth, rightdepth)
    @staticmethod
    def diameter(root):
        if root is None:
            return 0
        leftdepth = FindDepth.maxdepth(root.left)
        rightdepth = FindDepth.maxdepth(root.right)

        leftdiameter = FindDepth.diameter(root.left)
        rightdiameter = FindDepth.diameter(root.right)

        return max(leftdepth + rightdepth, max(leftdiameter , rightdiameter))
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Calculate the maximum depth
fd = FindDepth()
diameter = fd.diameter(root)

print("Maximum diameter of the binary tree:", diameter)
