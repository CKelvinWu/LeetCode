// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        def addSum(root, vals, sum):
            if root is None:
                return 0
            
            vals += root.val
            
            if root.left and root.right:                
                return addSum(root.left, vals, sum) or addSum(root.right, vals, sum)
                              
            elif root.right is None and root.left:
                return addSum(root.left, vals, sum)
            elif root.left is None and root.right:
                return addSum(root.right, vals, sum)
            else:
                return sum == vals
            
        if not root:
            return False
        result, vals = [], 0
        
        # print(addSum(root, vals, sum))
        return addSum(root, vals, sum)