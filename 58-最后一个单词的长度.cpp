class Solution {
public:
    int lengthOfLastWord(string s) {
        int lens=s.size();
        int flag=0;
        int ans=0;
        for(int i=lens-1;i>=0;i--)
        {
            if(s[i]!=' ')
            {
                ans++;
                flag=1;
            }
            if(s[i]==' '&&flag==1)
                break;
        }
        return ans;
    }
};