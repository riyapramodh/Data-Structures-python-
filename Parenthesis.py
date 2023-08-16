#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here

        stack = []
        for i in range(len(x)):
            if x[i] in "({[":
                stack.append(x[i])
            elif x[i] in ")}]":
                if not stack:
                    return False
                gundu = stack.pop()
                if (x[i] == ")" and gundu != "(") or \
                    (x[i] == "]" and gundu != "[") or \
                    (x[i] == "}" and gundu != "{") :
                    return False

        return len(stack) == 0
