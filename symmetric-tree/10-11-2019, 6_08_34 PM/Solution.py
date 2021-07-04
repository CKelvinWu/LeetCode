// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        
        if root is None:
            return True        
        return self.symRoot(root.left, root.right)        
    
    def symRoot(self, leftroot, rightroot):
        if leftroot is None and rightroot is None:
            return True
        if leftroot is not None and rightroot is not None:
            return leftroot.val == rightroot.val and self.symRoot(leftroot.left,rightroot.right) and self.symRoot(leftroot.right,rightroot.left)
                
        