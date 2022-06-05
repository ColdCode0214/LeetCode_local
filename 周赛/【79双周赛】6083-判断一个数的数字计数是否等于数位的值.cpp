class Solution {
public:
    bool digitCount(string num) {
        int lens=num.size();
        unordered_map<int, int> mp;
        for(int i=0;i<lens;i++)
        {
            int temp=num[i]-48;
            mp[temp]++;
        }
        for(int i=0;i<lens;i++)
        {
            int temp=num[i]-48;
            if(mp[i]!=temp)
                return false;
        }
        // for(auto& a:mp)
        // {
        //     if (a.first!=a.second)
        //         return false;
        // }
        return true;
    }
};
