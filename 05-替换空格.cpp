class Solution {
public:
    string replaceSpace(string s) {
        string ans="";
        string temp="%20";
        for(int i=0;i<s.size();i++)
        {
            if(s[i]==' ')
                ans+=temp;
            else
                ans+=s[i];
        }
        return ans;
    }
};
