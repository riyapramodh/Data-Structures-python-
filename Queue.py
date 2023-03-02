#queue using classes
#1.)

import collections
queue = collections.deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
queue.popleft()
print(queue)
print(not queue)
print(queue[-1])
print(queue[0])


#2.)
import queue
q = queue.Queue()
q.put(11)
q.put(22)
q.put(33)
q.put(44)
print(q)
q.get()
q.get()
print(q)
