class Node:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None

def VerticalOrder(root):
    if root is None:
        return
    verticallevel = {}
    queue = [(root,0)] #node and its level(horizontal level)

    while queue:
        node,level = queue.pop(0) #dequeue
        if level in verticallevel: #if the level that we dequeued is in the dict already then to that particular level (consider list) we append the node value
            verticallevel[level].append(node.data)
        else: #we create a new space for that particular level in the dict and store the corresponding node value
            verticallevel[level] = [node.data]

        if node.left:
            queue.append((node.left,level-1))
        if node.right:
            queue.append((node.right,level+1))


        for level in sorted(verticallevel):
            print(verticallevel[level]) #*operator prints each element as if it isnt in the dict

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(9)

# Perform vertical order traversal
VerticalOrder(root)

