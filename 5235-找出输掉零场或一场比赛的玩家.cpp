class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        map<int, int> mp;
        int lens=matches.size();
        for(int i=0;i<lens;i++)
        {
            mp[matches[i][0]];
            mp[matches[i][1]]++;
        }
        vector<int> ans1, ans2;
        vector<vector<int>> ans;
        for(auto& a:mp)
        {
            if(a.second==0)
                ans1.push_back(a.first);
            if(a.second==1)
                ans2.push_back(a.first);
        }
        ans.push_back(ans1);
        ans.push_back(ans2);
        return ans;
    }
};
