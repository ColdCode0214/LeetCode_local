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
    void inorder(TreeNode* root, vector<int> &res)
    {
        if(root==nullptr)
            return;
        inorder(root->left, res);
        res.push_back(root->val);
        inorder(root->right, res);
    }
    TreeNode* increasingBST(TreeNode* root) {
        vector<int> res;
        inorder(root, res);

        TreeNode* dummyNode=new TreeNode(-1);
        TreeNode* curNode=dummyNode;
        for(int value:res)
        {
            curNode->right=new TreeNode(value);
            curNode=curNode->right;
        }
        return dummyNode->right;
    }
};
