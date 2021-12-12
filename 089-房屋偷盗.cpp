class Solution {
public:
    int rob(vector<int>& nums) {
        int lens=nums.size();
        if(lens==1)
            return nums[0];
        int ans[lens+1];
        ans[0]=0,ans[1]=nums[0];
        for(int i=2;i<=lens;i++)
            ans[i]=max(ans[i-1], ans[i-2]+nums[i-1]);
        return ans[lens];
    }
};
