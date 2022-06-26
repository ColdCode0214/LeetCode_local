class Solution {
public:
    int countHousePlacements(int n) {
        int dp[n][2];
        dp[0][0]=1, dp[0][1]=1;
        for(int i=1;i<n;i++)
        {
            dp[i][0]=(dp[i-1][0]%1000000007+dp[i-1][1]%1000000007)%1000000007;
            dp[i][1]=dp[i-1][0];
        }
        long long int ans=(dp[n-1][0]%1000000007+dp[n-1][1]%1000000007)%1000000007;
        return (ans*ans)%1000000007;
    }
};
