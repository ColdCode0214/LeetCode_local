class Solution {
public:
    int purchasePlans(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int lens=nums.size();
        int l=0, r=lens-1;
        int ans=0;
        while(l<r)
        {
            if(nums[l]+nums[r]>target)
            {
                r--;
            }
            else
            {
                ans+=(r-l);
                ans%=1000000007;
                l++;
            }
        }
        return ans;
    }
};
