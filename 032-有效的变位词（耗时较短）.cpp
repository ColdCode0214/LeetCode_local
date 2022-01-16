class Solution {
public:
    bool isAnagram(string s, string t) {
        int l1=s.size(), l2=t.size();
        if(l1!=l2 || s==t)
            return false;
        int cnt[26]={0};
        for(int i=0;i<l1;i++)
        {
            if(s[i]!=t[i])
            {
                cnt[s[i]-'a']++;
                cnt[t[i]-'a']--;
            }
        }
        for(int i=0;i<26;i++)
            if(cnt[i]!=0)
                return false;
        return true;
    }
};
