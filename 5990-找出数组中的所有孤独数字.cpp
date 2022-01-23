class Solution {
public:
    vector<int> findLonely(vector<int>& nums) {
        int lens=nums.size();
        sort(nums.begin(), nums.end());
        vector<int> ans;
        unordered_map<int, int> mp;
        for(auto a:nums)
        {
            mp[a]++;
        }
        for(auto a:mp)
        {
            if(a.second==1 && !mp.count(a.first-1) && !mp.count(a.first+1))
                ans.push_back(a.first);
        }
        return ans;
    }
};
