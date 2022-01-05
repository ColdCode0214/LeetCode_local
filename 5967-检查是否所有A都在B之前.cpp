class Solution {
public:
    bool checkString(string s) {
        int lens=s.size();
        int flag=0;
        for(int i=0;i<lens;i++)
        {
            if(s[i]=='b')
                flag=1;
            if(flag==1 && s[i]=='a')
                return false;
                
        }
        return true;
    }
};
