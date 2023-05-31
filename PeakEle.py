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

    def bsearch(arr,n):
        low = 0
        high = n-2
        if n==1:
            return 0
        if arr[0]>arr[1]:
            return 0
        if arr[n-1]>arr[n-2]:
            return n-1
        while low<=high:
            mid = (low+high)//2
            if arr[mid+1]>arr[mid]:
                low = mid+1
            elif arr[mid-1]>arr[mid]:
                high = mid -1
            else:
                return mid
        return -1

print(naive([10,7,8,12,20],5))
print(search([10,7,8,12,20],5))
