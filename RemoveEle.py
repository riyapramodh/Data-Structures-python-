class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i] #we just swap the non matching ele to the index of what the count is 
                count+=1
        
        return count
