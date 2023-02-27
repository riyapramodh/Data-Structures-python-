#LIST

list = [1,2.3,"riya"]
LIST = ["riya",1,2.3]
print(type(list))
print(list == LIST)
print(list[-1]) #negative indices
list1 = [[1,2],3,4] #nested list
print(list1)
list1.append(9) #muttable
print(list1)
print(len(list1))
list1.remove(9)#list is dynamic
print(len(list1))

#TUPLE

tuple1 = (1,2,3,4)
print(type(tuple))
TUPLE = tuple()
print(TUPLE)
tuple2 = (2,)
print(tuple2)
#tuples are immutable

