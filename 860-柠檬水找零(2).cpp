class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int lens=bills.size();
        int count5=0,count10=0;
        bool ans=true;
        for(int i=0;i<lens;i++)
        {
            if(bills[i]==5)
                count5++;
            if(bills[i]==10)
            {
                count5--;
                count10++;
            }
            if(bills[i]==20)
            {
                if(count10>=1&&count5>=1)
                {
                    count10--;
                    count5--;
                }
                else
                    count5-=3;
            }
            if(count10<0||count5<0)
            {
                ans=false;
                break;
            }
        }
        return ans;
    }
};
