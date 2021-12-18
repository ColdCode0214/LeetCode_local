class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int low=0, high=0, ans=0;
        int lens=prices.size();
        for(int i=1;i<lens;i++)
        {
            if(prices[i]<prices[low])
                low=i;
            if(prices[i]>prices[i-1])
            {
                high=i;
                ans=max(ans, prices[high]-prices[low]);
            }
        }
        return ans;
    }
};
