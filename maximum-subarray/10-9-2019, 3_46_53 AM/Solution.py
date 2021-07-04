// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        if max(nums) < 0:
            return max(nums)
        
        local_max, global_max = 0, 0
        
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(local_max, global_max)
            
        return global_max
    
    
#         wrong code:

#         if not nums:
#             return []
#         newnums = []
        
#         for i in range(len(nums)):
#             sum = 0
#             for j in range(1,len(nums)-i+1,1):                
#                 sum += nums[i+j-1]
#                 newnums.append(sum)
                
#         return max(newnums)
            
            
            
                
                
