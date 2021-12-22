class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> mp;
        int lens=nums.size();
        for(auto& a:nums)
        {
            mp[a]++;
            if(mp[a]>lens/2)
                return a;
        }
        return -1;
    }
};
