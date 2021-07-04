// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.toBST(nums,0,len(nums)-1)
    
    def toBST(self,nums, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.toBST(nums,start,mid-1)
        node.right = self.toBST(nums, mid+1, end)
        return node
            
        