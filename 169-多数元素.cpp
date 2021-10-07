class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int lens=nums.size();
        sort(nums.begin(),nums.end());
        return nums[lens/2];
    }
};
