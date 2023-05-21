#sorting an array with three elements
#array has 0,1,2 and we use the Dutch National Flag Algorithm to solve this

def threeele(arr):
    low = 0
    mid = 0
    n = len(arr)
    high = n-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr

print(threeele([0,1,1,0,1,2,1,2,0,0,0]))
