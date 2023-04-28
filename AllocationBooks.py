def possible(arr,mid,k,n):
    student = 1
    pages = 0
    for i in range(0,n):
        if arr[i] > mid:
            return False
        if pages + arr[i] > mid:
            student += 1
            pages += arr[i]
        else:
            pages += arr[i]
    if student>k:
        return False
    return True

def check(arr,n,k):
    low = min(arr)
    high = sum(arr)

    while low<=high:
        mid = (low+high)//2
        if possible(arr,mid,k,n):

            high = mid - 1
        else:
            low = mid + 1
    return low

print(check([12,34,67,90],4,2))
