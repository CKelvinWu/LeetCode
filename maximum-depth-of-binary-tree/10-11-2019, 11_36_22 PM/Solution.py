// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        i = 1   
        
        return self.depth(root, i)
    
    def depth(self, root, i):
        if root.left is not None and root.right is not None:
            i += 1
            return max(self.depth(root.left,i),self.depth(root.right,i))
        elif root.left is not None and root.right is None:
            i += 1
            return self.depth(root.left,i)
        elif root.left is None and root.right is not None:
            i += 1
            return self.depth(root.right,i)
        
        return i

    
        
        
