def ms(arr,low,high):

    if low==high:
        return 0
    else:
        mid = (low+high)//2

    ms(arr,low,mid)
    ms(arr,mid+1,high)
    merge(arr,low,mid,high)
    return arr

def merge(arr,low,mid,high):

    temp = []
    left = low
    right = mid+1
    while left<=mid and right<=high:
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left +=1
        else:
            temp.append(arr[right])
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
    return arr

print(ms([3,1,4,2,1,5,2,6,4],0,8))


