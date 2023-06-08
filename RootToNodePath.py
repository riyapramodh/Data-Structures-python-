# Definition for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root, target, path, found):
    # Base case: If the root is None or the target is found
    if root is None or found:
        return found

    # Recursive call for the left subtree
    found = inorder(root.left, target, path, found)

    # Add the current node to the path
    path.append(root.data)

    # If the current node matches the target, print the path and set the found flag to True
    if root.data == target:
        print("Root to Node Path:", path)
        found = True

    # Recursive call for the right subtree
    found = inorder(root.right, target, path, found)

    # Remove the current node from the path
    path.pop()

    return found

# Example usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Set the target node value
target = 5

# Initialize an empty list to store the path
path = []

# Initialize a boolean flag to track if the target is found
found = False

# Call the inorder function to print the root to node path
found = inorder(root, target, path, found)
