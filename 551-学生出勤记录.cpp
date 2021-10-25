class Solution {
public:
    bool checkRecord(string s) {
        int lens=s.size();
        if(lens==1)
            return true;
        int count_a=0;
        for(int i=0;i<lens;i++)
        {
            if(s[i]=='A')
                count_a++;
            if(count_a>1)
                return false;
            if(i>=2 && s[i]=='L' && s[i-1]=='L' && s[i-2]=='L')
                return false;
        }
        return true;
    }
};
