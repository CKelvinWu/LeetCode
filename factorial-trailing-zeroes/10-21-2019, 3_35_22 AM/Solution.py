// https://leetcode.com/problems/factorial-trailing-zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        result, i = 0, 1
        while 5**i <= n:
            result += n//5**i
            i += 1
        return result