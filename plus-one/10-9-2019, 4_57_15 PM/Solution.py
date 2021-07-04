// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        
        digits[len(digits)-1] = digits[len(digits)-1] +1        
        carry = digits[len(digits)-1] // 10
        digits[len(digits)-1] %= 10
        
        for i in range(len(digits)-2,-1,-1):
            digits[i] += carry
            carry = digits[i] // 10 
            digits[i] %= 10            
        if carry > 0:
            digits.insert(0,carry)
        return digits