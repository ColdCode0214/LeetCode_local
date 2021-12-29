class Solution {
public:
    int countBalls(int lowLimit, int highLimit) {
        unordered_map<int, int> mp;
        int temp=0,sum=0,ans=0;
        for(int i=lowLimit;i<=highLimit;i++)
        {
            temp=i;
            sum=0;
            while(temp>0)
            {
                sum+=temp%10;
                temp/=10;
            }
            mp[sum]++;
            ans=max(ans, mp[sum]);
        }
        return ans;
    }
};
