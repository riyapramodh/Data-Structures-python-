#to rotate an array by k elements to the right


#method 1
def reverse(nums,start,end):
    while start<= end:
        nums[start],start[end] = start[end],start[start] #thru swapping it acheives the rotation purpose
        start+=1
        end-=1

def rotate(nums,k):
    n = len(nums)
    k = k%n #to handle k values larger than that of n
    reverse(nums,0,n-1)# reverse the entire array
    reverse(nums,0,k-1)#then reverse the first k ele in the reversed array
    reverse(nums,k,n-1)#followed by reversing the k -n ---> remaining ele in the array
    
    
    
    
    
#method2
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        start = 0
        end = n - 1
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        start = 0
        end = k - 1
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        start = k
        end = n - 1
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


