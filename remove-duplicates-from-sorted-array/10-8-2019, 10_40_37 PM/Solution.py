// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        
        if not nums:
            return 0
        
        count = 0
        
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count+1
    
            
            
        
        # while k <= len(nums):
        #     try:
        #         if nums[k] == nums[k+1]:
        #             del nums[k]
        #         else:
        #             k += 1
        #     except Exception as e:
        #         break
        # return len(nums)