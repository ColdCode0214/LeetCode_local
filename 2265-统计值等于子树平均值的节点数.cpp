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
    int averageOfSubtree(TreeNode* root) {
        if(root==nullptr)
            return 0;
        int ans=0;
        return root->val==sum(root)/num(root) ? averageOfSubtree(root->left)+averageOfSubtree(root->right)+1 : averageOfSubtree(root->left)+averageOfSubtree(root->right);
        
    }
    int sum(TreeNode* root)
    {
        if(root==nullptr)
            return 0;
        return root->val+sum(root->left)+sum(root->right);
    }
    int num(TreeNode* root)//统计该root下共有多少节点
    {
        if(root==nullptr)
            return 0;
        // if(root->left==nullptr && root->right==nullptr)
        //     return root->val;
        int ans=1+num(root->left)+num(root->right);
        return ans;
    }
};
