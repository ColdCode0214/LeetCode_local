class Solution {
public:
    int minimumCost(vector<int>& cost) {
        int lens=cost.size();
        sort(cost.begin(), cost.end());
        int ans=0;
        int count=1;
        for(int i=lens-1;i>=0;i--)
        {
            if(count<3)
            {
                ans+=cost[i];
                count++;
            }
            else
            {
                count=1;
            }
        }
        return ans;
    }
};
