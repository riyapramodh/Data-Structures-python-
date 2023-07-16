from collections import deque
def zigzag(root):
    if root is None:
        return None
    queue = deque()
    queue.append(root)
    zigzag = []
    leftright = True
    while queue :
        levelnodes = []
        levelsize = len(queue)
        for i in range(levelsize):
            node = queue.popleft()
            queue.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if leftright :
                zigzag.append(levelnodes)
            else:
                zigzag.append(levelnodes[::-1])
                leftright = not leftright
    return zigzag
