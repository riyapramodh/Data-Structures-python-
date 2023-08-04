class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # arr = []
        # n1 = len(nums1)
        # n2 = len(nums2)
        # n = max(n1,n2)
        # for i in range(0,n):
        #     if nums1[i] in nums2:
        #         arr.append(nums1[i])
        #         nums2.remove(nums1[i])
        # return arr
        
        nums1.sort()
        nums2.sort()
        arr = []
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0
        while i<n1 and j<n2:
            if nums1[i] == nums2[j]:
                arr.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return arr
            
        
        
