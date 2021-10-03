
class Solution {
public:
    string licenseKeyFormatting(string s, int k) {
        int lens=s.size();
        string ans="";
        int count=0;
        for(int i=lens-1;i>=0;i--)
        {
            if(s[i]!='-')
            {
                ans.push_back(toupper(s[i]));
                count++;
                if(count%k==0)
                    ans.push_back('-');
            }
        }
        if(ans.back()=='-')
            ans.pop_back();
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
