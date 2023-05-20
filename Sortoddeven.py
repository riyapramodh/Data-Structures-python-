#sorting an array with different types of elements:
#sorting odd and even numbers such that it puts the even numbers first then the odd numbers
#here instead of pivot we use the odd or even calculation
def sort(arr,low,high):
    if low<=high:
        p = oddeven(arr,low,high)
        sort(arr,low,p-1)
        sort(arr,p+1,high)
    return arr

def oddeven(arr,low,high):
    i = low
    j = high
    while i<j:
        if arr[i]%2==0 and i<=high:#instead of pivot we use (%2 ==0) or (%2 !=0)
            i+=1
        if arr[j]%2!=0 and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j

print(sort([15,14,13,12],0,3))
