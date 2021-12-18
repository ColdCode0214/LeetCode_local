class Solution {
public:
    int waysToChange(int n) {
        int dp[n+1];
        int coin[4]={1,5,10,25};
        for(int i=0;i<n+1;i++)
            dp[i]=0;
        dp[0]=1;
        for(int i=0;i<4;i++)
        {
            for(int j=coin[i];j<=n;j++)
            {
                dp[j]=dp[j]+dp[j-coin[i]];
                dp[j]%=1000000007;
            }
            
        }
        return dp[n];
    }
};
