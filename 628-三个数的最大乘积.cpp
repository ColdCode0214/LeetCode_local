class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int lens=nums.size();
        return max(nums[0]*nums[1]*nums[lens-1], nums[lens-1]*nums[lens-2]*nums[lens-3]);
    }
};
