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
    int height(TreeNode*root)
    {
        if(root==nullptr)
            return 0;
        int leftHeight=height(root->left);
        int rightHeight=height(root->right);
        if(leftHeight==-1 || rightHeight==-1 || abs(leftHeight-rightHeight)>1)
            return -1;
        else
            return max(leftHeight, rightHeight)+1;
    }

    bool isBalanced(TreeNode* root) {
        return height(root)>=0;
    }
};
