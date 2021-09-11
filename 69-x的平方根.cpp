class Solution {
public:
    int mySqrt(int x) {
        int ans=0;
        if(x<=6)
        {
            for(int i=0;i<=x;i++)
            {
                if(i*i>x)
                {
                    ans=i-1;
                    break;
                }
                else if(i*i==x)
                {
                    ans=i;
                    break;
                }
            }
            return ans;
        }

        for(long long int i=0;i<=x/2;i++)
        {
            if(i*i>x)
            {
                ans=i-1;
                break;
            }
            else if(i*i==x)
            {
                ans=i;
                break;
            }
        }
        return ans;
    }
};