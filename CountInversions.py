def ms(arr,low,high):
    count = 0
    if low == high:
        return count

    mid = (low+high)//2

    count += ms(arr,low,mid)
    count += ms(arr,mid+1,high)
    count += merge(arr,low,mid,high)
    return count

def merge(arr,low,mid,high):
    count = 0
    temp = []
    left = low
    right = mid+1
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left +=1
        else:
            temp.append(arr[right])
            count += mid - left + 1
            right+=1

    #if there are still elements remaining on the left beacuse the right<=high conditions becomes False since that side runs out of elements we need to copy the remaining left side elements onto the temp array
    while left<=mid:
        temp.append(arr[left])
        left+=1

    #if there are still elements remaing on the right because the condition left<=mid becomes false in the main loop since the left side of array ran out of elements we need to append the remaining right side elements onto the temp array
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low, high+1):
        arr[i] = temp[i-low]
    return count
# def countinversions(arr):
#     return ms(arr,0,len(arr)-1)

print(ms([4,3,2,1],0,3))

