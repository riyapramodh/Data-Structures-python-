class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        if len(strs) ==1:
            return prefix
         
    
        for s in strs:
            i = 0
            while i<len(s) and i<len(prefix) and prefix[i] == s[i]:
                i+=1
            prefix = prefix[:i]
        if not prefix:
            return ""
        return prefix


        
        
        
        
