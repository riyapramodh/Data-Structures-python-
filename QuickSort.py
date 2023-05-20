#we first find the pivot then we use two pointers and see if there is an element bigger than pivot using low pointer:YES, check for the smallest element using the high pointer 
#we swap their values and if NO, we just proceed with the iteartion
#if high crosses low we stop there and bring the pivot to the posititon where we stopped
def partitionIndex(arr,low,high):
    i = low
    j = high
    pivot = arr[low]
    while i<j:
        while arr[i]<= pivot and i<=high-1:
            i+=1
        while arr[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]#when i is less than j we swap places of i which is on the left to the right with the places of j which is on the right to the left because i is searching for bigger ele than pivot and needs to be placed on the right whereas the j pointer searches for smaller ele and it shud be placed on the left of the pivot
         
    arr[low],arr[j] = arr[j],arr[low]#ehrn j crosses i and ïf"condition fails it automatically swaps the place of your pivot with that of the j location and one set is said to have been completed
    return j

def quicksort(arr,low,high):
    if low<=high:
        pIndex = partitionIndex(arr,low,high)
        quicksort(arr,low,pIndex-1)
        quicksort(arr,pIndex+1,high)
    return arr

print(quicksort([4,6,2,5,7,9,1,3],0,7))
