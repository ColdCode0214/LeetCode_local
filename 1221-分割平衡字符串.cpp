class Solution {
public:
    int balancedStringSplit(string s) {
        int lens=s.size();
        int count_l=0, count_r=0;
        int ans=0;
        for(int i=0;i<lens;i++)
        {
            if(s[i]=='L')
            {
                count_l++;
            }
            if(s[i]=='R')
            {
                count_r++;
            }
            if(count_l==count_r)
            {
                count_l=0;
                count_r=0;
                ans++;
            }
        }
        return ans;
    }
};
