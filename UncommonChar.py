#given two strings we need to return the chars that are uncommon bw them two
class Solution:
    def UncommonChars(self,A, B):
        #code here
        result = ""
        re= ""
        for i in A:
            if i not in B:
                result +=i
        for j in B:
            if j not in A:
                result+=j
        result = set(result)
        
        for k in sorted(result):
            re +=k
        if len(re)>0:
            return re
        return -1
        
