class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        int lens=nums.size();
        if(lens<=1)
            return 1;
        sort(nums.begin(), nums.end());
        int ans=1;
        int pre=nums[0];
        for(int i=1;i<lens;i++)
        {
            if(nums[i]-pre>k)
            {
                ans++;
                pre=nums[i];
            }
        }
        return ans;
    }
};
