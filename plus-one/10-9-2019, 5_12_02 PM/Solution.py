// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        
        digits.insert(0,1)
        return digits
        
        # carry = 1        
        # for i in reversed(range(len(digits))):
        #     digits[i] += carry
        #     carry = digits[i] // 10 
        #     digits[i] %= 10            
        # if carry > 0:
        #     digits.insert(0,carry)
        # return digits