#method1
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_depth(root):
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)

# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Calculate the maximum depth
depth = max_depth(root)

print("Maximum depth of the binary tree:", depth)




#meth2

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
        return 1+max(leftdepth,rightdepth)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Calculate the maximum depth
fd = FindDepth()
depth = fd.maxdepth(root)

print("Maximum depth of the binary tree:", depth)
