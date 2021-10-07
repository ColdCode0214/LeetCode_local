class Solution {
public:
    int massage(vector<int>& nums) {
        int lens=nums.size();
        if(lens==0)
            return 0;
        if(lens==1)
            return nums[0];
        int dp0=0,dp1=nums[0],temp0=0,temp1=0;
        for(int i=1;i<lens;i++)
        {
            temp0=max(dp0,dp1);
            temp1=dp0+nums[i];
            dp0=temp0;
            dp1=temp1;
        }
        return max(dp0,dp1);
    }
};
