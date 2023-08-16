#we need to reverse a substring as in like for example:
#Input: s = "the sky is blue"
#Output: "blue is sky the"


#we must remove extra spaces
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split()
        print(arr)
        return " ".join(arr[::-1])
       
 
