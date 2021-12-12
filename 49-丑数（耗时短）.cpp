class Solution {
public:
    int nthUglyNumber(int n) {
        int p2=0, p3=0, p5=0;
        int dp[n];
        dp[0]=1;
        for(int i=1;i<n;i++)
        {
            int a2=dp[p2]*2, a3=dp[p3]*3, a5=dp[p5]*5;
            dp[i]=min(min(a2, a3), a5);
            if(a2==dp[i])
                p2++;
            if(a3==dp[i])
                p3++;
            if(a5==dp[i])
                p5++;
        }
        return dp[n-1];
    }
};
