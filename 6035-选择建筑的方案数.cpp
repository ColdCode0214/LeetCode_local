class Solution {
public:
    long long numberOfWays(string s) {
        int c0=0, c1=0;
        int lens=s.size();
        for(int i=0;i<lens;i++)
        {
            if(s[i]=='0')
                c0++;
            else
                c1++;
        }
        int temp0=0, temp1=0;
        long long int ans=0;
        for(int i=0;i<lens;i++)
        {
            if(s[i]=='0')
            {
                temp0++;
                ans+=(temp1*(c1-temp1));
            }
            else
            {
                temp1++;
                ans+=(temp0*(c0-temp0));
            }
        }
        return ans;
    }
};
