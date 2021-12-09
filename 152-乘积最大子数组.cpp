class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int lens=nums.size();
        int f_min[lens], f_max[lens];
        f_min[0]=nums[0], f_max[0]=nums[0];
        int res=nums[0];
        for(int i=1;i<lens;i++)
        {
            f_min[i]=min(min(f_min[i-1]*nums[i], nums[i]), f_max[i-1]*nums[i]);
            f_max[i]=max(max(f_min[i-1]*nums[i], nums[i]), f_max[i-1]*nums[i]);
            res=max(res, max(f_max[i], f_min[i]));
        }
        return res;
    }
};
