// https://leetcode.com/problems/path-sum

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
    bool hasPathSum(TreeNode* root, int sum) {
        if(!root) return false;
        
        queue<TreeNode*> Q;
        queue<int> qsum;
        Q.push(root);
        qsum.push(root->val);
        
        while(!Q.empty()){
            TreeNode* temp_root = Q.front();
            int temp_sum = qsum.front();
            Q.pop();
            qsum.pop();
            if(!temp_root->left && !temp_root->right){
                if(sum == temp_sum) return true;
            }
            if(temp_root->left){
                Q.push(temp_root->left);
                qsum.push(temp_sum + temp_root->left->val);
            }
            if(temp_root->right){
                Q.push(temp_root->right);
                qsum.push(temp_sum + temp_root->right->val);
            }
        }
        return false;
    }
};