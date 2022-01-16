class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        int lens=deck.size();
        if(lens==1)
            return false;
        unordered_map<int, int> mp;
        int m=0;
        for(auto& a:deck)
        {
            mp[a]++;
            m=max(m, mp[a]);
        }
        if(m==1)
            return false;
        int temp=0, ans=m;
        for(int i=0;i<deck.size()-1;i++)
        {
            //cout<<"i:"<<mp[deck[i]]<<"     i+1:"<<mp[deck[i+1]]<<endl;
            temp=gcd(mp[deck[i]], mp[deck[i+1]]);
            ans=min(temp, ans);
            //cout<<"ans*:"<<ans<<endl;
        }
        //cout<<"ans:"<<ans<<endl;
        return ans>=2;
    }
};
