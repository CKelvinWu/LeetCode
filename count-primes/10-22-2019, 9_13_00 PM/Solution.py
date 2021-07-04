// https://leetcode.com/problems/count-primes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        nums = [True]*n
        nums[0] = nums[1] = False
        for i in range(n):
            if nums[i] == True:
                for j in range(i*i, n, i):
                    nums[j] = False
        return sum(nums)
            