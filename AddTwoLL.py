# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Initialize a variable to keep track of carry.
        carry = 0
        
        # Initialize a dummy node for the result linked list.
        dummy = ListNode()
        
        # 'curr' will be used to traverse the result linked list.
        curr = dummy

        # Loop until both l1 and l2 are exhausted, and there is no carry.
        while l1 or l2 or carry:
            # Get the values from l1 and l2. If any list is exhausted, use 0 as the value.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the current digits and the carry from the previous step.
            total = val1 + val2 + carry

            # Determine the carry for the next step (if any).
            carry = total // 10

            # Create a new node with the current digit and attach it to the result linked list.
            curr.next = ListNode(total % 10)

            # Move 'curr' to the newly created node.
            curr = curr.next

            # Move to the next nodes in l1 and l2, if they exist.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the next node of the dummy node, which contains the result linked list.
        return dummy.next
