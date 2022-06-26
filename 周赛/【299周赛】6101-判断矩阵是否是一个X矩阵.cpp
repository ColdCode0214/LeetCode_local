class Solution {
public:
    bool checkXMatrix(vector<vector<int>>& grid) {
        int lens=grid.size();
        for(int i=0;i<lens;i++)
        {
            for(int j=0;j<lens;j++)
            {
                if((i==j)||(i+j==lens-1))
                {
                    if(grid[i][j]==0)
                        return false;
                }
                else
                {
                    if(grid[i][j]!=0)
                        return false;
                }
            }
        }
        return true;
    }
};
