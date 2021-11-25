class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int lens=position.size();
        int sum1=0, sum0=0;
        for(int i=0;i<lens;i++)
        {
            if(position[i]%2==1)
                sum1++;
            else
                sum0++;
        }
        return min(sum1, sum0);
    }
};
