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
            //�����ǰ�ڵ���Ҷ�ӽ��
            if(root->left==nullptr && root->right==nullptr)
                paths.push_back(path);
            else//��ǰ�ڵ㲻��Ҷ�ӽڵ�
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
