#hash table method to see if the sum of two num in an array is eq to target:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hasht = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in hasht:
                return [hasht[x],i]
            else:
                hasht[num] = i
            
        return []

