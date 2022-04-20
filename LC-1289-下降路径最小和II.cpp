class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int lens=grid.size();
        if(lens==1)
            return grid[0][0];
        vector<vector<int>> dp;
        vector<int> temp;
        int min1=0, indexj=0;//注意此处min1初始化应该为0而不是grid[0][0]，因为在while循环中还会初始化一次
        int min2=0;
        for(int i=0;i<lens;i++)
        {
            int premin1=min1;
            int prej=indexj;
            //每到新的一行，min1需重置
            if(indexj==0)
            {
                min1+=grid[i][1];
                indexj=1;
            }
            else
            {
                min1+=grid[i][0];
                indexj=0;
            }
            temp.clear();
            for(int j=0;j<lens;j++)
            {
                if(i==0)
                    temp.push_back(grid[i][j]);
                else
                {
                    if(j==prej)
                        temp.push_back(min2+grid[i][j]);
                    else
                        temp.push_back(premin1+grid[i][j]);
                }

                if(temp[j]<min1)
                {
                    min1=temp[j];
                    indexj=j;
                }

            }

            dp.push_back(temp);
            sort(temp.begin(), temp.end());
            min2=temp[1];

        }

        return min1;
    }
};
