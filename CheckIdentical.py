class Node:
    def __init__(self,data):
        self.data = data
        self.lef = None
        self.right = None
        
def identical(root1,root2):
    if root1 and root2:
        return True
    elif root1 or root2:
        return False
    else:
        return (
            root1 == root2
            and identical(root1.left,root2.left)
            and identical(root1.right,root2.right)
        )
