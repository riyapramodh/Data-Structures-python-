#printing an array
def print_array(arr1):
    print("printing the array")
    index = 0
    while index < len(arr1):
        print(arr1[index])
        index +=1

print_array([1,2,3,4])



#insertion --> inserting an element in the kth position
def array_insert():
    arr2 = [1,2,3,4,5]
    print("the array is:",arr2)
    print("enter the number you want to insert:")
    a = int(input())
    print("enetr the position at which u want to enter:")
    b = int(input())
    arr2[b] = a
    print(arr2)

array_insert()

#array deletion
def array_del():
    arr3 = [10,20,30,40,50]
    print(arr3)
    print("enter the array element you want to delete:")
    c = int(input())
    if c in arr3:
        arr3.remove(c)
        print(arr3)
    else:
        print("invalid aray element!")
array_del()
