#sorting an array with different types of elements:
#sorting negative and positive elements such that we have to put the negative numbers first then positive

#may come in any (unordered) manner and is the naive solution
def naive(arr):
    temp = []
    n = len(arr)
    for i in range(0,n):
        if arr[i]<0:
            temp.append(arr[i])

    for j in range(0,n-1):
        if arr[j]>=0:
            temp.append(arr[j])
    return temp
print(naive([1,4,-1,-4,2,-5]))
#comes in an ordered manner and is the efficient solution
def complex(arr,low,high):
    if low<=high:
        p = pIndex(arr,low,high)
        complex(arr,low,p-1)
        complex(arr,p+1,high)
    return arr

def pIndex(arr,low,high):
    i = low
    j = high
    pivot = arr[low]
    while i<j:
        if arr[i]<=pivot and i<=high-1:
            i+=1
        if arr[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j
print(complex([1,4,-1,-4,2,-5],0,5))
