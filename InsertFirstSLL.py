class Node: #creating a node
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:#linking the multiple nodes using a forward reference storing capacity
    def __init__(self):
        self.head = None
    def print_LL(self):#printing of array
        if self.head is None:
            print("the linked list is empty")
        else:
            n = self.head
            print(n)
            n = n.next
    def add_first(self, data):#adding a node to the front of the linked list
        new_node = Node(data)#calling an object for the class also its the first element
        new_node.next = self.head
        #new node next reference points to the head node but the refernce of the head node (prev first node) will be stored in head which is now stored in the new node
        #new node.next points to the the prev first node
        #new node then stores the head value of the previous node
        self.head = new_node
        print(new_node)

LL = LinkedList()
LL.add_first(10)
LL.add_first(20)
LL.print_LL()


#so the linked list will be like[20,10,..] as the last added one would be present in the first
