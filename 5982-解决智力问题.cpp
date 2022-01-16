class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        long long int ans=0;
        int lens=questions.size();
        long long int cp[lens][2];
        long long int dp[lens];
        for(int i=0;i<lens;i++)
        {
            cp[i][0]=questions[lens-1-i][0];
            cp[i][1]=questions[lens-1-i][1];
        }
        dp[0]=cp[0][0];
        for(int i=1;i<lens;i++)
        {
            if(i-cp[i][1]-1<0)
            {
                dp[i]=max(dp[i-1], cp[i][0]);
            }
            else
            {
                dp[i]=max(dp[i-1], dp[i-cp[i][1]-1]+cp[i][0]);
            }
        }
        return dp[lens-1];
    }
};
