class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        if(startFuel>=target)
            return 0;//如果起始时燃料足够多，则不需要加油
        int lens=stations.size();//一共有lens个加油站

        if(startFuel<target && lens==0)
            return -1;//如果起始时燃料不够多、路上没有加油站，则一定到不了目的地
        long long int dp[lens+1];//设dp[i]为加i次油能走的最远的距离，加油次数最多为加油站的次数+起点
        for(int i=0;i<lens+1;i++)
            dp[i]=0;
        dp[0]=startFuel;
        for(int i=0;i<lens;i++)
        {
            for(int j=i;j>=0;j--)
            {
                if(dp[j]>=stations[i][0])
                    dp[j+1]=max(dp[j+1], dp[j]+stations[i][1]);
            }
        }
        for(int i=0;i<lens+1;i++)
        {
            if(dp[i]>=target)
                return i;
        }
            
        return -1;
    }
};
