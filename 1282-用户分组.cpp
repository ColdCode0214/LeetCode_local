class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        vector<vector<int>> ans;
        int lens=groupSizes.size();
        vector<int> temp;
        map<int, vector<int>> mp;
        for(int i=0;i<lens;i++)
            mp[groupSizes[i]].push_back(i);
        for(auto& a:mp)
        {
            int n=a.second.size();
            for(int i=0;i<n;i+=a.first)
            {
                for(int j=i;j<i+a.first;j++)
                    temp.push_back(a.second[j]);
                ans.push_back(temp);
                temp.clear();
            }
        }
        return ans;
    }
};
