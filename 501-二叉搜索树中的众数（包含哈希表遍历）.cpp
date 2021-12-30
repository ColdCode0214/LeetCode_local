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
    void inorder(TreeNode* root, unordered_map<int, int> &res)
    {
        if(!root)
            return; 
        inorder(root->left, res);
        //res.push_back(root->val);
        res[root->val]++;
        inorder(root->right, res);
    }

    vector<int> findMode(TreeNode* root) {
        unordered_map<int, int> res;
        inorder(root, res);
        int count=0;
        for(auto& a:res)
        {
            if(a.second>count)
                count=a.second;
        }
        vector<int> ans;
        for(auto& a:res)
        {
            if(a.second==count)
                ans.push_back(a.first);
        }
        return ans;
    }
};
