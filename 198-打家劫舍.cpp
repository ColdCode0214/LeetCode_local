class Solution {
public:
    int rob(vector<int>& nums) {
        int lens=nums.size();
        if(lens==1)
            return nums[0];
        int dp[lens][2];
        dp[0][0]=0, dp[0][1]=nums[0];
        for(int i=1;i<lens;i++)
        {
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]);
            dp[i][1]=dp[i-1][0]+nums[i];
        }
        return max(dp[lens-1][0], dp[lens-1][1]);
    }
};
