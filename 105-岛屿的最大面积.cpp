class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m=grid.size(), n=grid[0].size();
        int ans=0;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(grid[i][j]==1)
                {
                    ans=max(ans, dfs(grid, i, j));
                }
            }
        }
        return ans;
    }

    int dfs(vector<vector<int>>& grid, int r, int c)
    {
        //int count=0;
        if(!inArea(grid, r, c) || grid[r][c]!=1)
            return 0;
        //count++;
        
        grid[r][c]=2;
        
        int count=1;
        count+=dfs(grid, r-1, c);
        count+=dfs(grid, r+1, c);
        count+=dfs(grid, r, c-1);
        count+=dfs(grid, r, c+1);
        return count;
    }

    bool inArea(vector<vector<int>>& grid, int r, int c)
    {
        return 0<=r && r<grid.size() && 0<=c && c<grid[0].size();
    }
};

//¾­µäÌâ½â£ºhttps://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/ 
