class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m=matrix.size(), n=matrix[0].size();
        int flag_m[m], flag_n[n];
        for(int i=0;i<m;i++)
            flag_m[i]=0;
        for(int j=0;j<n;j++)
            flag_n[j]=0;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(matrix[i][j]==0)
                {
                    flag_m[i]=1;
                    flag_n[j]=1;
                }
            }
        }
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(flag_m[i]==1 || flag_n[j]==1)
                    matrix[i][j]=0;
            }
        }
    }
};
