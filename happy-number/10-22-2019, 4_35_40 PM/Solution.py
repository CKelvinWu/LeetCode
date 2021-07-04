// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        
        while n >= 10:
            sum = 0
            while n >= 1:
                sum += (n%10)**2
                n //= 10
            n = sum
                
        if n == 1 or n == 7:
            return True
        else:
            return False