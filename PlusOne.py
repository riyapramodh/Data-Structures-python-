class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        carry = 1
        for i in range(n-1,-1,-1):
            
            digits[i]+=carry
            carry = digits[i]//10 
            digits[i]%=10
            
        if carry:
            digits.insert(0,carry)
        return digits

# Inside the loop, we perform the following steps for each digit in reverse order (from right to left):

# a. We add the carry value to the current digit. This effectively adds 1 to the digit, which is what we want to achieve.

# b. We update the carry value by dividing the sum of the current digit and the carry by 10. The result of this division will be either 0 (no carry) or 1 (carry).

# c. We update the current digit by taking the modulo (%) of the sum of the current digit and the carry with 10. This ensures that the current digit stays within the range of 0 to 9.

# After the loop is complete, we have successfully added 1 to the number represented by the digits list. If there is any remaining carry value (i.e., carry == 1), it means the number was originally all 9's, and we need to add one more digit at the beginning of the digits list.
        
        
        
        
        
#.................................................................................................................................................................      
#         n = len(digits)
#         if len(digits) == 1 and digits[0] == 9:
#             digits[0]=1
#             digits.append(0)
#         for i in range(n-1,0,-1):
#             if digits[i]+1>9:
#                 digits[i-1]=1
#                 digits[i] = 0
#                 i-=1
#             else:
#                 digits[i]+1
#                 break
                

#         return digits
    
  #..........................................................................................................................................  
    
#         elif digits[n-1] == 9:
#             digits[n-2]+=1
#             digits[n-1] = 0
        
#         else:
#             digits[n-1]+=1
        
