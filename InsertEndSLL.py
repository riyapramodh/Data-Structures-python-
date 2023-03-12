class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("the LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(new_node)
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node


LL = LinkedList()
LL.add_begin(10)
LL.add_begin(20)
LL.add_end(100)
LL.print_LL()
