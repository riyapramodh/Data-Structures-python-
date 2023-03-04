#prriority que is not based on FIFO but based on priority
#normal way
q = []
q.append(20)
q.append(50)
q.append(10)
print(q)
q.sort()
print(q)
#for popingout the greater value elements (as bellow) and for lesser value elements (q.popleft())
q.pop()
q.pop()
print(q)


#using priority queue
import queue
q = queue.PriorityQueue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)
q.put(40)#removing the same priority element as in here the number 40 will be done based on the order of it in the queue
print(q)
q.get()#lowest numbers will be removed automatically irrespective of wheather we perform sorting or not
#takes lowest value as the highest priority

#using tuple to set priority for an element
juice = []
juice.append((1,"mogu mogu"))
juice.append((10,"cavins"))
juice.append((2,"al-maraih"))
print(juice)
juice.sort()
juice.pop()#pops out the numbers in ascending order as the priority
juice.sort(reverse = True)
juice.pop()#pop out the numbers as the descending order as priority

