def kth(nums,,k):
    def partitions(nums,low,high):
        pivot = nums[high] #choosing a pivot suvh that (evtg to its left < than pivot) and (evtg to its right>pivot)
        i = low
        for j in range(low,high):
            if nums[j]>pivot:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        nums[i],nums[high] = nums[high],nums[i] #accordingly swaps are made to make it suitable to the initiallty mentioned condition to be satisfied
        return i

    n = len(nums)
    low = 0
    high = n-1
    while True:
        p = partitions(nums,low,high)
        if p == k-1: #if the partion inex = p and k (k-1 since arr count starts from 0) are the same then we just return that particular element at that index
            return nums[k-1]
        elif p>k-1: #if the index is greater than k, we need to keep that as the end since k lies within that index
            high  = p-1
        else:#if the index is lesser than k then we make it the start as k would be found only aftr from that particular index
            low = p+1



def naive(nums,k):
  nums.sort()
  nums.reverse()
  return nums[k-1]
