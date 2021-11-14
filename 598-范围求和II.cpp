class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        int lens=ops.size();
        if(lens==0)
            return m*n;
        int row=ops[0][0], col=ops[0][1];
        for(int i=0;i<lens;i++)
        {
            row=min(row,ops[i][0]);
            col=min(col,ops[i][1]);
        }
        return min(row,m)*min(col,n);
    }
};
