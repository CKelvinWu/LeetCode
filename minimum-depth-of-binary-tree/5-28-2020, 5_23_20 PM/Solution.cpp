// https://leetcode.com/problems/minimum-depth-of-binary-tree

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
    
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> Q;
        Q.push(root);
        int count = 0;
        while(!Q.empty()){
            count++;
            int Q_size = Q.size();
            for (int j = 0; j < Q_size; j++){
                TreeNode *temp_root = Q.front();
                Q.pop();
                if (!temp_root->left && !temp_root->right) return count;
                if (temp_root->left) Q.push(temp_root->left);
                if (temp_root->right) Q.push(temp_root->right);
            }
        }
        return -1;
        
    }
};