class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int lens=nums.size();
        int dp[lens];
        int ans=1;

        for(int i=0;i<lens;i++)
        {
            dp[i]=1;
            for(int j=0;j<i;j++)
            {
                if(nums[i]>nums[j])
                {
                    dp[i]=max(dp[i], dp[j]+1);
                    if(dp[i]>ans)
                        ans=dp[i];
                }
            }
        }
        return ans;
    }
};
