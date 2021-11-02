class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lens=prices.size();
        if(lens==1)
            return 0;
        int dp[lens][3];
        dp[0][0]=0, dp[0][1]=-prices[0], dp[0][2]=0;
        for(int i=1;i<lens;i++)
        {
            dp[i][0]=max(dp[i-1][0], dp[i-1][2]);
            dp[i][1]=max(dp[i-1][1], dp[i-1][0]-prices[i]);
            dp[i][2]=dp[i-1][1]+prices[i];
        }
        return max(dp[lens-1][0], dp[lens-1][2]);
    }
};
