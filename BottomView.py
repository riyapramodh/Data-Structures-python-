from collections import deque

# Definition for a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottom_view(root):
    # Base case: If the tree is empty
    if root is None:
        return []

    # Create a queue for level order traversal
    queue = deque()
    queue.append((root, 0))  # Tuple of (node, horizontal distance)
    
    # Create a dictionary to store the horizontal distance and corresponding node value
    hd_dict = {}

    while queue:
        node, hd = queue.popleft()

        # Update the horizontal distance in the dictionary
        hd_dict[hd] = node.data

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Sort the dictionary based on the horizontal distance
    sorted_hd_dict = sorted(hd_dict.items(), key=lambda x: x[0])

    # Extract the node values from the sorted dictionary
    bottom_view = [val for _, val in sorted_hd_dict]

    return bottom_view

# Example usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

# Perform bottom view traversal
result = bottom_view(root)
print(result)
