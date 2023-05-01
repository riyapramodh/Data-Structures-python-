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
        if arr[mid]>=arr[low]:#means your middle element is greater than the first element and hence the left side is sorted...in either ways we need to find which side is sorted and now we find it out as such
            if x >= arr[low] and x<= arr[mid-1]:#since left is sorted we see if x is greater than first element and lesser than mid value, it lies on the left
                high = mid - 1#else we see on the right side which is the unsorted side though
            else:
                low = mid + 1
        if arr[mid]<=arr[high]:#Means your mid is lesser than the last element and u can say that your right side is sorted while your left side is not
            if x <= arr[high] and x<= arr[mid]:# we see if the x is greater than mid but lesser than the highest vale on the sorted right hand side
                low = mid + 1
            else:
                high = mid - 1#if not we set boundaries and search for it on the unsorted lefthand side
    return -1

print(search([10,70,40,60,5,8],5,6))
