// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        
        return int(x**0.5)
        # for i in range(x//2+2):
        #     if i**2 < x and (i+1)**2 >x or i**2 == x:
        #         return i
        
            