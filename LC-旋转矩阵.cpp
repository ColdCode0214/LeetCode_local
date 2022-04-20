class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int lens=matrix.size();
        int temp=0;
        for(int i=0;i<lens;i++)
        {
            for(int j=i;j<lens-1-i;j++)
            {
                temp=matrix[i][j];
                matrix[i][j]=matrix[lens-1-j][i];
                matrix[lens-1-j][i]=matrix[lens-1-i][lens-1-j];
                matrix[lens-1-i][lens-1-j]=matrix[j][lens-1-i];
                matrix[j][lens-1-i]=temp;
            }
        }
    }
};
