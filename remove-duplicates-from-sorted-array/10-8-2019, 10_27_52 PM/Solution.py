// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        
        k =0
        while k <= len(nums):
            try:
                if nums[k] == nums[k+1]:
                    del nums[k]
                else:
                    k += 1
            except Exception as e:
                break
        return len(nums)