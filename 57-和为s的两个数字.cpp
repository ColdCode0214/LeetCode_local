class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int lens=nums.size();
        int left=0, right=lens-1;
        vector<int> ans;
        while(left<right)
        {
            if(nums[left]+nums[right]==target)
            {
                ans.push_back(nums[left]);
                ans.push_back(nums[right]);
                return ans;
            }

            else if(nums[left]+nums[right]>target)
                right--;
            else
                left++;
        }
        return ans;
    }
};
