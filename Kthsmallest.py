#return the kth smallest ele in an array
def naive(arr,k):
    n = len(arr)
    arr.sort()
    return arr[k-1]

print(naive([1,5,8,3,9,2],4))

def kindex(arr,low,high,k):
    n = len(arr)
    while low<=high:
        p = findp(arr,low,high)
        kindex(arr,low,p-1,k)
        kindex(arr,p+1,high,k)
        if p==k-1:
            if arr[p-1]!=arr[p]:#checking for dupliacte 2,2,3
                return arr[p]#if no duplicates 2,3 just print the [th index ele
            else:#if dupliactes are present 2,2,3 it shud print the p+1th index
                return arr[p+1]
        if p>k-1:
            high = p-1
        else:
            low = p+1
    return 0


def findp(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>pivot and j >=low+1:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j


print(kindex([1,5,8,3,9,2],0,5,4))

