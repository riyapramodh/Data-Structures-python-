#to find the subarray within the array that has the max value for the sum

#we use the approach that the 'sum' only stores a value if it is greater than 0; hence not taking forward any negative numbers;
#then we compare the sum with max; if sum>max we update max but if sum is not > max the we return that particular max value

import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max = -sys.maxsize - 1 #the maximum value it can hold and - indicates the large negative value it can store; sub by 1 indicates that it should stay in range of the given numbers
        for i in range(len(nums)):
            sum += nums[i]
            if sum>max:
                max = sum
            if sum<0:
                sum = 0
        return max
            
   
