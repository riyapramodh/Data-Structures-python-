#every ele in an array occurs 2 times, if it occurs just once we need to return that array
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()#to make it easy
        pre = []
        count = 0
        n = len(nums)
        i = 0
        while i<=n: #here n is just len(nums) and not len(nums)-1 because we have a seperate condition (i==n-1) that makes sure that it doesnt go or appear as array out of bounds
            if i == n-1 or nums[i]!=nums[i+1]: #boundary conditions occur measn we assume that it doesnt repeat twice
                return nums[i]
            i+=2
        return -1
            
            # pre.append(nums[i])
            # count+=1
            # if count<2 and nums[i] != nums[i+1]:
            #     return nums[i]
            # elif i = n-1:
            #     return nums[i]
            # elif count<2 and nums[i] == nums[i+1] :
            #     i+=1
            #     continue
            # else:
            #     i+=1
            #     count = 0
            
                
            
                
        
