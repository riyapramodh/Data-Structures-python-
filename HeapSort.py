#heap sort
def siftDown(arr,i,upper):
    while True: #inorder to avoid the use of multiple recurssions
        l = 2*i+1
        r = 2*i+2
        if max(l,r)<upper:#two child nodes are present for the parent node also upper is the portion to consider
            if arr[i] >= max(arr[l],arr[r]):
                break#means the parent is greater than both the child
            #if parent is not greater then we see which child is greater than the parent
            elif arr[l]>arr[r]:#to check if the left child is greater than the right child
                arr[i],arr[l] = arr[l],arr[i]
                i = l
            else:
                arr[i],arr[r] = arr[r],arr[i]
                i = r
        elif l<upper:#only one child is present(the left child)
            if arr[l]>arr[i]:#since only one child is present we see if that is greater than the parent
                arr[i],arr[l] = arr[l],arr[i]
                i = l
            else: break
        elif r<upper:#only one child is present(the right child)
            if arr[r]>arr[i]:#since only one child is present we see if that is greater than the parent
                arr[i],arr[r] = arr[r],arr[i]
                i = r
            else: break
        else: break


def heapSort(arr):
    for j in range((len(arr)-2)//2,-1,-1):
        siftDown(arr,j,len(arr))
    for end in range(len(arr)-1,0,-1):
        arr[0],arr[end] = arr[end],arr[0]
        siftDown(arr,0,end)
    return arr


print(heapSort([5,16,8,14,20,1,26]))




