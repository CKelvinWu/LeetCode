// https://leetcode.com/problems/path-sum-iii

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pathSum(TreeNode* root, int sum) {
        if (!root) return 0;
        return sumUp(root, sum) + pathSum(root->left, sum) + pathSum(root->right, sum);
    }
    int sumUp(TreeNode* root, int sum) {
        if (!root) return 0;
        return (curr == root->val) + sumUp(root->left, sum - root->val) + sumUp(root->right, sum - root->val);
    }
};