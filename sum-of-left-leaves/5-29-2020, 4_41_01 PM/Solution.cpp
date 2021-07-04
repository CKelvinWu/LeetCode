// https://leetcode.com/problems/sum-of-left-leaves

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
    // int sumOfLeftLeaves(TreeNode* root) {
    //     if (!root) return 0;
    //     int sum = 0;
    //     queue<TreeNode*> Q;
    //     Q.push(root);
    //     while(!Q.empty()) {
    //         TreeNode* temp = Q.front();
    //         Q.pop();            
    //         if(temp->left) {
    //             if (!temp->left->left && !temp->left->right) sum += temp->left->val;
    //             Q.push(temp->left);
    //         } 
    //         if(temp->right) {
    //             Q.push(temp->right);
    //         } 
    //     }
    //     return sum;
    // }
    
    int sumOfLeftLeaves(TreeNode* root) {
        if (!root) return 0;
        if (root->left && !root->left->left && !root->left->right) return root->left->val + sumOfLeftLeaves(root->right);
        return sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
    }
};