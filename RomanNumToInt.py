#METHOD 1

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        sums = 0
        s = s.replace("IV","IIII").replace("IX","VIIII")
        s = s.replace("XL","XXXX").replace("XC","LXXXX")
        s = s.replace("CD","CCCC").replace("CM","DCCCC")
        for char in s:
            sums+=d[char]
        
        return sums
#METHOD 2

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        sums = 0
        for i in range(0,len(s)):
            if i<len(s)-1 and d[s[i]]<d[s[i+1]]:
                sums -=d[s[i]]
            else:
                sums += d[s[i]]
        return sums

