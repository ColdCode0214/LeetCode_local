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
    int dfs(TreeNode* root, unordered_map<int, int> &mp)
    {
        if(!root)
            return 0;
        int count=0;
        count+=dfs(root->left, mp);
        if(!mp.count(root->val))
        {
            count++;
            mp[root->val]=1;
        }
        count+=dfs(root->right, mp);
        return count;
    }

    int numColor(TreeNode* root) {
        int count=0;
        unordered_map<int, int> mp;
        count=dfs(root, mp);
        return count;
    }
};
