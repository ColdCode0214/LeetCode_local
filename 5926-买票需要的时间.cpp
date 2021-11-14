class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int lens=tickets.size();
        int ans=0;
        for(int i=0;i<lens;i++)
        {
            if(i<=k)
                ans+=min(tickets[i],tickets[k]);
            else
                ans+=min(tickets[i],tickets[k]-1);
        }
        return ans;
    }
};
