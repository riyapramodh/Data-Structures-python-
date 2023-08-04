class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pre = []
        # for i in range(0,len(nums)):
        #     if nums[i] not in  pre:
        #         pre.append(nums[i])
        #     else:
        #         return True
        # return False
        
        nums.sort()
        Flag = False
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                Flag = True
                break
        return Flag
            
        
