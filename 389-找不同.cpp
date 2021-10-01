class Solution {
public:
    char findTheDifference(string s, string t) {
        int lens=s.size();
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        for(int i=0;i<lens;i++)
        {
            if(s[i]!=t[i])
                return t[i];
        }
        return t[lens];
    }
};
