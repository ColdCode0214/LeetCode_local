class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int lens=nums.size();
        k=k%lens;
        vector<int> ans;
        for(int i=lens-k;i<lens;i++)
            ans.push_back(nums[i]);
        for(int i=0;i<lens-k;i++)
            ans.push_back(nums[i]);
        for(int i=0;i<lens;i++)
            nums[i]=ans[i];
    }
};
