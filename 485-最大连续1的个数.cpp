class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int lens=nums.size();
        int dp[lens];
        for(int i=0;i<lens;i++)
            dp[i]=0;
        dp[0]=nums[0];
        int ans=dp[0];
        for(int i=1;i<lens;i++)
        {
            if(nums[i]==1)
            {
                dp[i]=dp[i-1]+1;
                ans=max(ans, dp[i]);
            }
            else
            {
                dp[i]=0;
            }
        }
        return ans;
    }
};
