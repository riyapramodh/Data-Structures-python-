def naive(arr,n):
    if n==1:
        return arr[0]
    if arr[0]>arr[1]:
        return arr[0]
    if arr[n-1]>arr[n-2]:
        return arr[n-1]
    for i in range(n):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            return arr[i]
    return -1

def search(arr,n):
    low = 0
    high = n-1
    mid = (low+high)//2
    while low<= high:
        if arr[low]>arr[1]:
            return arr[low]
        if arr[high]>arr[n-2]:
            return arr[high]
        if arr[mid]>arr[mid-1]and arr[mid]>arr[mid+1]:
            return arr[mid]
        if arr[mid-1]>arr[mid]:
            high = mid -1
        else:
            low = mid + 1
        if arr[mid]<arr[mid + 1]:
            low = mid + 1
        else:
            high = mid -1
    return -1

print(naive([10,7,8,12,20],5))
print(search([10,7,8,12,20],5))
