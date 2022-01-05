/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* dummy=new TreeNode(-1);
    TreeNode* cur=dummy;
    TreeNode* convertBiNode(TreeNode* root) {
        dummy->right=root;
        dfs(root);
        return dummy->right;
    }
    void dfs(TreeNode* root)
    {
        if(!root)
            return;
        dfs(root->left);
        root->left=nullptr;
        cur->right=root;
        cur=root;
        dfs(root->right);
    }
};
