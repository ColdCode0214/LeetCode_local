class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int lens=nums.size();
        vector<int> ans;
        for(int i=0;i<lens;i++)
        {
            if(nums[i]==target)
                ans.push_back(i);
        }
        return ans;
    }
};
