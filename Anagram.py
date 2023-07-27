#to see if two strings are anagrams of each other
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        chart = {}
        chars = {}
        for char in s:
            chars[char] = chars.get(char,0)+1
        for char in t:
            chart[char] = chart.get(char,0)+1
        return chart == chars
        
