class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int lens=triangle.size();
        if(lens==0)
            return 0;
        int dp[lens][lens];
        for(int i=0;i<lens;i++)
        {
            for(int j=0;j<=i;j++)
            {
                if(i==0)
                    dp[i][j]=triangle[i][j];
                else if(j==0)
                    dp[i][j]=dp[i-1][j]+triangle[i][j];
                else if(j==i)
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j];
                else
                    dp[i][j]=min(dp[i-1][j], dp[i-1][j-1])+triangle[i][j];
            }
        }
        int ans=dp[lens-1][0];
        /*
        for(int i=0;i<lens;i++)
        {
            for(int j=0;j<=i;j++)
            {
                cout<<dp[i][j]<<" ";
            }
            cout<<endl;
        }*/
        
        for(int i=1;i<lens;i++)
            ans=min(ans, dp[lens-1][i]);

        return ans;
    }
};
