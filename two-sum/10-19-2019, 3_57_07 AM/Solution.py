// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}        
        for index, value in enumerate(nums):
            sub = target - nums[index]
            if sub not in dic:
                dic[value] = index
            else:
                return[dic[sub], index]