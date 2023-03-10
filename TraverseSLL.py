#linkdlist --> need not be in a contiguos manner
#traversal add and delete elements from linked list from beggining end or in between the existing nodes
class Node: #for creating an initial node
    def __init__(self,data):
        self.data = data
        self.next = None #initially it will be none ; node1 = Node()

class LinkedList: #for linking the nodes that would be added or already present
    def __init__(self):
        self.head = None #empty linked list can perform insert or delete
    def print_LL(self):
        if self.head == None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next
LL1 = LinkedList() #creating an object
LL1.print_LL()
