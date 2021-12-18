class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size(), n=grid[0].size();
        if(m==0 || n==0)
            return 0;
        int dp[m][n];
        dp[0][0]=grid[0][0];

        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(i==0 && j!=0)//��һ�е�·����ֻ����������ߵ�Ԫ�أ���һ��Ԫ�س���
                    dp[i][j]=dp[i][j-1]+grid[i][j];
                else if(j==0 && i!=0)//��һ�е�·��ֻ�����������Ԫ�أ���һ��Ԫ�س���
                    dp[i][j]=dp[i-1][j]+grid[i][j];
                else if(i!=0 && j!=0)
                    dp[i][j]=min(dp[i-1][j], dp[i][j-1])+grid[i][j];
            }
        }
        return dp[m-1][n-1];
    }
};
