// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):   
    
        def sortArray(nums, start, end):
            if start > end:
                return None
            mid = (start + end)//2          
            root = TreeNode(nums[mid])
            root.left = sortArray(nums, start, mid-1)
            root.right = sortArray(nums, mid+1, end)
            return root;
        
        return sortArray(nums, 0, len(nums)-1)