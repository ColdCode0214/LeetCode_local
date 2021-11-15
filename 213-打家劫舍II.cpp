class Solution {
public:
    int rob(vector<int>& nums) {
        int lens=nums.size();
        if(lens==1)
            return nums[0];
        if(lens==2)
            return max(nums[0], nums[1]);
        if(lens==3)
            return max(nums[0], max(nums[1], nums[2]));
        int a1=nums[0], b1=max(nums[0], nums[1]), c1=0;
        int a2=nums[1], b2=max(nums[1], nums[2]), c2=0;
        for(int i=2;i<lens-1;i++)
        {
            c1=max(a1+nums[i], b1);
            a1=b1;
            b1=c1;
        }
        for(int i=3;i<lens;i++)
        {
            c2=max(a2+nums[i], b2);
            a2=b2;
            b2=c2;
        }
        return max(c1, c2);
    }
};
