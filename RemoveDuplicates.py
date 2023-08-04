#to remove duplicates from the sorted array and just print the array alone 
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(0,len(nums)):
            if i<len(nums)-1 and nums[i] == nums[i+1]:
                continue
            nums[count] = nums[i]
            count +=1
        return count
