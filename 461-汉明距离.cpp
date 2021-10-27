class Solution {
public:
    int hammingDistance(int x, int y) {
        uint32_t a=x, b=y;
        uint32_t ans=a^b;
        int count=0;
        while(ans>0)
        {
            if(ans%2==1)
                count++;
            ans/=2;
        }
        return count;
    }
};
