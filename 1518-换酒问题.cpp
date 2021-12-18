class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int ans=0;
        int temp=0;
        while(numBottles>=numExchange)
        {
            temp=numBottles/numExchange;
            numBottles=numBottles-temp*numExchange+temp;
            ans+=temp*numExchange;
        }
        ans+=numBottles;
        return ans;
    }
};
