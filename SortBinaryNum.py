#sorting an array with different types of elements:
#sorting binary numbers such that we put 0s first and then the 1s

def sort(arr,low,high):
    if low<=high:
        p = pIndex(arr,low,high)
        sort(arr,low,p-1)
        sort(arr,p+1,high)
    return arr

def pIndex(arr,low,high):
    i = low
    j = high
    pivot = arr[low]
    while i<j:
        if arr[i]==0 and i<=high-1:
            i+=1
        if arr[j]==1 and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low], arr[j] = arr[j],arr[low]
    return j

print(sort([1,1,0,0,1,0,1,1],0,7))
