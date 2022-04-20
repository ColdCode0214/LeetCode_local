class Solution {
public:
    long long waysToBuyPensPencils(int total, int cost1, int cost2) {
        long long int ans=0;
        int lens=total/cost1;
        for(int i=0;i<=lens;i++)
        {
            ans+=(total-i*cost1)/cost2+1;
        }
        return ans;
    }
};
