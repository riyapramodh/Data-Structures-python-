def naive(arr,x):
    i = 0
    while arr[i]<x:
        if arr[i] == x:
            return i
        return -1



def search(arr,x,n):
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        if arr[mid]>=arr[low]:
            if x >= arr[low] and x<= arr[mid-1]:
                high = mid - 1
            else:
                low = mid + 1
        if arr[mid]<=arr[high]:
            if x <= arr[high] and x<= arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(search([10,70,40,60,5,8],5,6))
