class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
        int lens=nums.size();
        if(lens==1)
            return 0;
        if(lens==2)
        {
            if(nums[1]==0)
                return 0;
            if(nums[0]==0)
                return 1;
            else
                return -1;
        }
        int ans=0;
        int sum_l=0,sum_r=0;
        for(int i=1;i<lens;i++)
            sum_r+=nums[i];
        while(sum_l!=sum_r&&ans<lens-1)
        {
            sum_l+=nums[ans];
            ans++;
            sum_r-=nums[ans];
        }
        if(sum_l==sum_r)
            return ans;
        else
            return -1;
    }
};