#collections --> deque

import collections
stack = collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
print(stack[-1])
stack.pop()
print(stack)
stack.pop()
stack.pop()
print(not stack)

#queue --> lifoqueue

import queue
stack1 = queue.LifoQueue()
stack1.put(11)
stack1.put(22)
print(stack1)
stack1.get()
stack1.get()
print(not stack1)
