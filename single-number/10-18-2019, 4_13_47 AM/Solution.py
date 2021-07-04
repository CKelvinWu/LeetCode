// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        k = 0
        for i in nums:
            k ^= i
        return k
        
        # if nums[0] not in nums[1:]:
        #     return nums[0]
        # else:
        #     nums.remove(nums.pop(0))
        #     return self.singleNumber(nums)
                