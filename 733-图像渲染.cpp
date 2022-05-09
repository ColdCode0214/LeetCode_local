class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int k=image[sr][sc];
        
        int m=image.size(), n=image[0].size();
        vector<vector<int>> flag;
        vector<int> temp;
        for(int j=0;j<n;j++)
            temp.push_back(0);
        for(int i=0;i<m;i++)
            flag.push_back(temp);
        dfs(image, sr, sc, k, flag, newColor);

        return image;
    }

    void dfs(vector<vector<int>>& image, int r, int c, int k, vector<vector<int>> flag, int newColor)
    {
        if(!inArea(image, r, c) || image[r][c]!=k || flag[r][c]!=0)
            return;
        
        image[r][c]=newColor;
        flag[r][c]=1;

        dfs(image, r-1, c, k, flag, newColor);
        dfs(image, r+1, c, k, flag, newColor);
        dfs(image, r, c-1, k, flag, newColor);
        dfs(image, r, c+1, k, flag, newColor);
    }

    bool inArea(vector<vector<int>>& image, int r, int c)
    {
        return 0<=r && r<image.size() && 0<=c && c<=image[0].size();
    }
};
