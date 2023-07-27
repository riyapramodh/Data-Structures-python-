class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charcount = {}
        for char in s:
            charcount[char] = charcount.get(char,0)+1
        for i, char in enumerate(s):
            if charcount[char] == 1:
                return i
        return -1
    
                
        
