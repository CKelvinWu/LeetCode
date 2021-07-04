// https://leetcode.com/problems/factorial-trailing-zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        i = 1
        result = 0
        while 5**i <= n:
            result = result + n//(5**i)
            i += 1
        return result