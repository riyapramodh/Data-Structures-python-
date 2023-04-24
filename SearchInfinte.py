def naive(arr,x):
    i = 0
    while arr[i] <= x:
        if arr[i] == x:
            return i
        else:
            i +=1
    return -1


def bsearch(arr,x,l,h):
    low = l
    high = h
    while low<= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            high = mid -1
        else:
            low = mid+1
    return -1

def search(arr,x):
    if arr[0] == x:
        return 0
    i = 1
    while arr[i]<x:
        i = i*2
    if arr[i]==x:
        return i
    bsearch(arr,x,i//2,i)


print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 17, 19, 21, 23, 25, 30, 43, 47, 50, 55, 59, 60, 66, 69, 70, 71], 11))
print(naive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 17, 19, 21, 23, 25, 30, 43, 47, 50, 55, 59, 60, 66, 69, 70, 71], 11))
