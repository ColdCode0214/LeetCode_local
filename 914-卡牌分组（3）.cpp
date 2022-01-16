class Solution {
    int cnt[10000];
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        for(auto& a:deck)
            cnt[a]++;

        int ans=cnt[deck[0]];
        for(int i=0;i<10000;i++)
            if(cnt[i])
                ans=gcd(cnt[i], ans);
        return ans>=2;
    }
};
