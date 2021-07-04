// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0
        for num in nums:
            sum1, sum2 = max(num+sum2, sum1), sum1
        return sum1