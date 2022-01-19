class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        int a=costs[0][0], b=costs[0][1], c=costs[0][2];
        int x=0, y=0, z=0;
        int lens=costs.size();
        for(int i=1;i<lens;i++)
        {
            x=costs[i][0]+min(b,c);
            y=costs[i][1]+min(a,c);
            z=costs[i][2]+min(a,b);
            a=x;
            b=y;
            c=z;
        }
        return min(a, min(b,c));
    }
};
