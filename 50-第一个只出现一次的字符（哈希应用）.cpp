class Solution {
public:
    char firstUniqChar(string s) {
        unordered_map<char, int> mp;
        for(auto& a:s)
        {
            if(mp.count(a))
                mp[a]++;
            else
                mp[a]=1;
        }

        for(int i=0;i<s.size();i++)
        {
            if(mp[s[i]]==1)
                return s[i];
        }
            
        return ' ';
    }
};
