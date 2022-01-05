class Solution {
public:
    string modifyString(string s) {
        int lens=s.size();
        for(int i=0;i<lens;i++)
        {
            if(s[i]=='?')
            {
                if(i-1>=0 && i+1<lens)
                {
                    s[i]='a';
                    if(s[i]==s[i-1] || s[i]==s[i+1])
                        s[i]='b';
                    if(s[i]==s[i-1] || s[i]==s[i+1])
                        s[i]='c';
                }
                else if(i-1>=0)
                {
                    s[i]='a';
                    if(s[i]==s[i-1])
                        s[i]='b';
                }
                else if(i+1<lens)
                {
                    s[i]='a';
                    if(s[i]==s[i+1])
                        s[i]='b';
                }
                else
                    s[i]='a';
            }
        }
        return s;
    }
};
