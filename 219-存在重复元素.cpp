class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> hm;
        int lens=nums.size();
        for(int i=0;i<lens;i++)
        {
            if(hm.count(nums[i]) && abs(hm[nums[i]]-i)<=k)
                return true;
            hm[nums[i]]=i;
        }
        return false;         
    }
};
