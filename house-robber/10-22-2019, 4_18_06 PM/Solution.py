// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0
        for i in range(len(nums)):
            sum1, sum2 = max(nums[i]+sum2, sum2), max(sum1, sum2)
        return max(sum1, sum2)