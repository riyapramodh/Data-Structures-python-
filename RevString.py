class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        low = 0
        n = len(s)
        high = n - 1
        while low < high:
            # Swap characters at low and high indices
            s[low], s[high] = s[high], s[low]
            # Move the pointers towards the middle
            low += 1
            high -= 1
