class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int lens=coins.size();
        int ans=0;
        int dp[amount+1];
        dp[0]=0;
        for(int i=1;i<=amount;i++)
            dp[i]=-1;
        for(int i=0;i<lens;i++)
        {
            for(int j=0;j<=amount;j++)
            {
                if(j>=coins[i])
                {
                    //cout<<"flag"<<endl;
                    if(dp[j-coins[i]]!=-1)
                    {
                        //cout<<"flag222"<<endl;
                        if(dp[j]==-1)
                            dp[j]=dp[j-coins[i]]+1;
                        else
                            dp[j]=min(dp[j-coins[i]]+1, dp[j]);
                    }
                }
            }
        }
        return dp[amount];
    }
};
