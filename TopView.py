#top view of a binary tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def topview(root):
    if root is None:
        return
    horizontaldist = {}
    queue = [(root,0)]#node value and its level value
    while queue: #exists
        node, level = queue.pop(0)
        if level not in horizontaldist:
            horizontaldist[level] = node.data
        if node.left:
            queue.append((node.left,level-1))
        if node.right:
            queue.append((node.right,level+1))
    for level in sorted(horizontaldist):
        print(horizontaldist[level],end = "")



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

print("the top view is:")
topview(root)
