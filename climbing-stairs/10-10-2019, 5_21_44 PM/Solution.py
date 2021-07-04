// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        
        times = n // 2
        i = 0
        sum = 0
        while i <= times:
            sum += self.stairs(n)/self.stairs(i)/self.stairs(n-i)
            n -= 1
            i += 1
        return int(sum)
        
        
        
    def stairs(self, n):
        if n <= 1:
            return 1
        for i in range(n-1):
            n *= (i+1)
        return n