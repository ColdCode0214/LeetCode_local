class Solution {
public:
    int cuttingRope(int n) {
        if(n<=2)
            return 1;
        int dp[n+1];
        for(int i=0;i<=3;i++)
            dp[i]=i;
        int temp=0;
        for(int i=4;i<=n;i++)
        {
            temp=i-1;
            for(int j=1;j<=i/2;j++)
            {
                temp=max(temp, dp[j]*dp[i-j]);
            }
            dp[i]=temp;
        }
        dp[2]=1, dp[3]=2;
        return dp[n];
    }
};
