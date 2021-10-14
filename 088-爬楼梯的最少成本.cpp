class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int lens=cost.size();
        if(lens==1)
            return 0;
        int sum[lens][2];//0-²»Ñ¡£¬1-Ñ¡
        sum[0][0]=0, sum[0][1]=cost[0];
        for(int i=1;i<lens;i++)
        {
            sum[i][0]=sum[i-1][1];
            sum[i][1]=min(sum[i-1][0],sum[i-1][1])+cost[i];
        }
        return min(sum[lens-1][0],sum[lens-1][1]);
    }
};
