class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(char.lower() for char in s if char.isalnum())
        n = len(s)
        low = 0
        high = n-1
        while low<=high:
            if s[low] == s[high]:
                low+=1
                high -=1
            else:
                return False
        return True
        
