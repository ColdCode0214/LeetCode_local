class Solution {
public:
    int jump(vector<int>& nums) {
        int lens=nums.size();
        int dp[lens];
        if(lens==1)
            return 0;
        dp[0]=0;
        for(int i=1;i<lens;i++)
        {
            int min=dp[i-1];
            for(int j=0;j<i;j++)
            {
                if(j+nums[j]>=i && dp[j]<min)
                    min=dp[j];
            }
            dp[i]=min+1;
        }
        return dp[lens-1];
    }
};
