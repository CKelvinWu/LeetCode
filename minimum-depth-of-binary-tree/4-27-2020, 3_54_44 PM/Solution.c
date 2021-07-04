// https://leetcode.com/problems/minimum-depth-of-binary-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int minDepth(struct TreeNode* root){
    int ldep, rdep;
    if (root == NULL){
        return 0;
    }
    if (root->left == NULL && root->right == NULL){
        return 1;
    }
    ldep = minDepth(root->left) + 1;
    rdep = minDepth(root->right) + 1;
    if(root->left != NULL && root->right != NULL){        
        return (ldep > rdep ? rdep : ldep);
    }
    return (ldep < rdep ? rdep : ldep);
}

