class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count=0;
        for(int i=0;i<grid.size();i++)
        {
            for(int j=0;j<grid[0].size();j++)
            {
                if(grid[i][j]=='1')
                {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        
        return count;
    }

    void dfs(vector<vector<char>>& grid, int r, int c)
    {
        //判断base case
        if(!inArea(grid, r, c))
            return ;
        
        if(grid[r][c]!='1')
            return ;

        grid[r][c]='2';
        
        //访问4个邻节点
        dfs(grid, r-1, c);
        dfs(grid, r+1, c);
        dfs(grid, r, c-1);
        dfs(grid, r, c+1);

        
    }

    bool inArea(vector<vector<char>>& grid, int r, int c)
    {
        return 0<=r && r<grid.size() && 0<=c && c<grid[0].size();
    }
};
