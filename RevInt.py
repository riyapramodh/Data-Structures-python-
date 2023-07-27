class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_num = 2**31 - 1
        min_num = -2**31
        reversed_num = 0
        if x>=0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
            
        while x!=0:
            reversed_num = reversed_num*10 + x%10
            x//=10
        
        reversed_num *= sign
        if reversed_num>max_num or reversed_num <min_num:
            return 0
        return reversed_num
        
