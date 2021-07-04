// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        
        # return int(x**0.5)
        if x < 2:
            return x
        
        left, right = 1, x // 2     
        
        while left <= right:
            mid = (left + right) // 2
            if mid  > x / mid:
                right = mid - 1
            else:
                left = mid + 1
                
        # if left == right:
        #     return right - 1            
        return right
                       
        
            
        # for i in range(x//2+1):
        #     if i**2 < x and (i+1)**2 >x or i**2 == x:
        #         return i
        
            