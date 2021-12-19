class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        int lens=prices.size();
        
        int dp[lens];
        dp[0]=1;
        long long int ans=dp[0];
        for(int i=1;i<lens;i++)
        {
            if(prices[i]+1==prices[i-1])
                dp[i]=dp[i-1]+1;
            else
                dp[i]=1;
            ans+=dp[i];
        }
        return ans;
    }
};
