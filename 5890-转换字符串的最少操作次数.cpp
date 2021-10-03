class Solution {
public:
    int minimumMoves(string s) {
        int lens=s.size();
        int ans=0;
        for(int i=0;i<lens;i++)
        {
            if(s[i]=='X')
            {
                ans++;
                s[i]='O';
                if(i<lens-1)
                    s[i+1]='O';
                if(i<lens-2)
                    s[i+2]='O';
            }
        }
        return ans;
    }
};
