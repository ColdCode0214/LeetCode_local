class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(auto& a:nums)
        {
            mp[a]++;
        }
        int ans=0;
        for(auto& a:nums)
            if(mp[a]==1)
                ans+=a;
        return ans;
    }
};
