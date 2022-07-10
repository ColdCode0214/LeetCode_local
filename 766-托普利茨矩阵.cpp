class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int m=matrix.size(), n=matrix[0].size();
        for(int i=0;i<m;i++)
        {
            int k=i, j=0;
            int sta=matrix[i][0];
            while(j<n&&k<m)
            {
                if(matrix[k][j]!=sta)
                {
                    cout<<"m:"<<matrix[k][j]<<endl;
                    return false;
                }
                k++;
                j++;
            }
        }
        for(int j=0;j<n;j++)
        {
            int k=j, i=0;
            int sta=matrix[0][j];
            while(i<m&&k<n)
            {
                if(matrix[i][k]!=sta)
                {
                    cout<<"m:"<<matrix[i][k]<<endl;
                    return false;
                }
                    
                k++;
                i++;
            }
        }
        return true;
    }
};
