class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int lens=nums.size();
        sort(nums.begin(), nums.end());
        return nums[lens-k];
    }
};
