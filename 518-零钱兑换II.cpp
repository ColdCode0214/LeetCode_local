class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int lens=coins.size();
        int ans=0;
        int dp[amount+1];
        for(int i=0;i<=amount;i++)
            dp[i]=0;
        dp[0]=1;
        for(int i=0;i<lens;i++)
        {
            for(int j=1;j<=amount;j++)
            {
                if(j>=coins[i])
                    dp[j]=dp[j]+dp[j-coins[i]];
            }
        }
        return dp[amount];
    }
};
