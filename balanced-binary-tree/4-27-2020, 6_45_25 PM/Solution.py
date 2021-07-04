// https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if root is None:
                return 0
            lheight, rheight = height(root.left), height(root.right)
            if lheight < 0 or rheight < 0 or abs(lheight-rheight) > 1:
                return -1            
            return max(height(root.left),height(root.right)) + 1
        
        return height(root) > -1
        
        
        
        
        