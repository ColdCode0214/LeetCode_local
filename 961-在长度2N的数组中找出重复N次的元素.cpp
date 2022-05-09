class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        map<int, int> mp;
        int n=nums.size()/2;
        for(auto& a:nums)
        {
            mp[a]++;
            if(mp[a]==n)
                return a;
        }
        return 0;
    }
};
