class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        unordered_map<int, int> mp;
        int m=0;
        for(auto& a:deck)
        {
            mp[a]++;
            m=max(m, mp[a]);
        }
        int flag=0;
        for(int i=2;i<=m;i++)
        {
            for(int j=0;j<deck.size();j++)
            {
                if(mp[deck[j]]%i!=0)
                {
                    break;
                }
                if(j==deck.size()-1)
                    flag=1;
            }
            if(flag==1)
                return true;
        }    
        return false;
    }
};
