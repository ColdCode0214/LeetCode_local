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
    void construct_paths(TreeNode* root, string path, vector<string> &paths)
    {
        if(root!=nullptr)
        {
            path+=to_string(root->val);
            //如果当前节点是叶子结点
            if(root->left==nullptr && root->right==nullptr)
                paths.push_back(path);
            else//当前节点不是叶子节点
            {
                path+="->";
                construct_paths(root->left, path, paths);
                construct_paths(root->right, path, paths);
            }
        } 
    }

    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> paths;
        construct_paths(root, "", paths);
        return paths;
    }
};
