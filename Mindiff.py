#here we find the minimum diff between two elements
#we use arr.sort than any sorting algorityhms as the main motive here is to find the difference so we may reduce the coding time

def mindifference(arr):
    arr.sort()
    n = len(arr)
    res = float('inf')
    for i in range(1,n):#we start from 1 cuz here we subtract ith element from its i- 1th element, so if we choose from 0 it wont have an i-1th element for it hence we begin with the 1st element
        res = min(res,(arr[i]-arr[i-1]))
    return res
print(mindifference([10,8,1,4]))
