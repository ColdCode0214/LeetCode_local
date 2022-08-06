class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        int total = 0;
        int lens=nums.size();
        for(int i=0;i<lens;i++)
            total += nums[i];
        sort(nums.begin(), nums.end());
        vector<int> ans;
        int count=0;
        for(int i=lens-1;i>=0;i--)
        {
            count+=nums[i];
            ans.push_back(nums[i]);
            if(count>total-count)
                return ans;
        }
        return ans;
    }
};
