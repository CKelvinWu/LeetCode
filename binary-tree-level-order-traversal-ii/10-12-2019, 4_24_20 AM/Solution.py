// https://leetcode.com/problems/binary-tree-level-order-traversal-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        
        if root is None:
            return[]
        
        result, curr = [], [root]
        while curr:
            next_level, vals = [], []
            for node in curr:
                vals += [node.val]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)            
            curr = next_level
            result.append(vals)
        
        return result[::-1]
