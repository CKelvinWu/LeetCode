// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution1:
        for i in range(k):
            nums.insert(0,nums.pop())
        
        # Solution2:
        # nums = nums[len(nums)-k:]+nums[:k+1]
        # for i in range(k):
            