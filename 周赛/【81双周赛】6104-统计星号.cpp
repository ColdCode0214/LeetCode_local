class Solution {
public:
    int countAsterisks(string s) {
        int lens=s.size();
        int ans=0;
        int count=0;
        for(int i=0;i<lens;i++)
        {
            if(s[i]=='|')
            {
                count++;
            }
            if(count%2==0)
            {
                if(s[i]=='*')
                {
                    ans++;
                }
            }
        }
        return ans;
    }
};
