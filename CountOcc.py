def firstocc(arr,x,n):
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>x:
            high = mid - 1
        elif arr[mid]<x:
            low = mid + 1
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                high = mid-1
    return -1
def lastocc(arr, x, n):
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>x:
            high  = mid - 1
        elif arr[mid]<x:
            low = mid + 1
        else:
            if mid == n-1 or arr[mid] != arr[mid+1]:
                return mid
            else:
                low = mid + 1
    return -1



def countocc(arr,x,n):
    ind = firstocc(arr,x,n)
    if ind == -1: #if in first occ element isnt present it returns -1 hence here we use that concept to see if the element is presenst or not

        return 0
    else:
        return lastocc(arr,x,n)-ind+1

print(countocc([1,2,3,3,3,3,3,4],3,8))


