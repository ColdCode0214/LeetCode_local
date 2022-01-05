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
    void inorder(TreeNode* root, vector<int> &res)
    {
        if(!root)
            return;
        inorder(root->left, res);
        res.push_back(root->val);
        inorder(root->right, res);
    }

    TreeNode* convertBiNode(TreeNode* root) {
        vector<int> res;
        inorder(root, res);
        TreeNode* dummyNode=new TreeNode(-1);
        TreeNode* cur=dummyNode;
        for(auto a:res)
        {
            cur->right=new TreeNode(a);
            cur=cur->right;
        }
        root=dummyNode->right;
        return root;
    }
};
