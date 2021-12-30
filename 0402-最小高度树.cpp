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
    TreeNode* inorder(vector<int> &nums, int left, int right)
    {
        if(left>right)
            return nullptr;
        int mid=left+(right-left)/2;
        TreeNode* mid_root=new TreeNode(nums[mid]);
        mid_root->left=inorder(nums, left, mid-1);
        mid_root->right=inorder(nums, mid+1, right);
        return mid_root;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        TreeNode* root=inorder(nums, 0, nums.size()-1);
        return root;
    }
};
