class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int lens=nums.size();
        if(lens==1)
            return 0;
        int f=nums[0], s=nums[1];
        int index=0;
        for(int i=0;i<lens;i++)
        {
            if(nums[i]>f)
            {
                s=f;
                f=nums[i];
                index=i;
            }
            if(nums[i]>s && nums[i]<f)
                s=nums[i];
        }
        if(s*2<=f)
            return index;
        else
            return -1;
    }
};
