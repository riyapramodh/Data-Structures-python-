class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def symmetry(root):
    if root is None:
        return
    else:
        return check(root.left,root.right)
def check(node_left,node_right):
    if node_left is None and node_right is None:
        return True
    if node_left is None or node_right is None or node_left.data!= node_right.data:
        return False

    return check(node_left.left,node_right.right) and check(node_left.right, node_right.left)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(5)
root.right.right = Node(4)

# Check if the binary tree is symmetric
result = symmetry(root)
print(result)
