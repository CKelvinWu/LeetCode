// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution1:
        k = k % len(nums)
        for i in range(k):
            nums.insert(0,nums.pop())
        
        # Solution2:
        # nums = nums[len(nums)-k:]+nums[:k+1]
        # if len(nums) != 1 and k != 0:
        #     nums.extend(nums[:k+1])
        #     del nums[:k+1]