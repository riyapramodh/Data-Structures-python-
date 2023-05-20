def chocolate(arr,m):#m is the number of children among whom the chocos need to be divided
    arr.sort()
    n = len(arr)
    if m>n:
        return -1
    res = arr[m-1]-arr[0]#after we sort the array we divide the chocs among the childrenn in the ascending order so that we may compute the diff bw the max and min chocs they got
    #initially we subtract from m-1 to 0 and as we go ahead to find more minimum difference the res value changes
    i = 1
    while (i+m-1)<n:
        res = min(res,(arr[i+m-1]-arr[i]))#here we keep moving one step ahead as one at atime to see and calculate the min difference calculated by the forward pairs
        i+=1
    return res
print(chocolate([7,3,2,4,9,12,56],3))
