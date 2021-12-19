class Solution {
public:
    int rob(vector<int>& nums) {
        int lens=nums.size();
        if(lens==0)
            return 0;
        if(lens==1)
            return nums[0];
        if(lens==2)
            return max(nums[0], nums[1]);
        int dp1[lens-1];
        dp1[0]=nums[0], dp1[1]=max(nums[0], nums[1]);
        int dp2[lens-1];
        dp2[0]=nums[1], dp2[1]=max(nums[1], nums[2]);
        for(int i=2;i<lens-1;i++)
        {
            dp1[i]=max(dp1[i-2]+nums[i], dp1[i-1]);
            dp2[i]=max(dp2[i-2]+nums[i+1], dp2[i-1]);
        }
        return max(dp1[lens-2], dp2[lens-2]);
    }
};
