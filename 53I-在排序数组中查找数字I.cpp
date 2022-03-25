class Solution {
public:
    int search(vector<int>& nums, int target) {
        int ans=0;
        int lens=nums.size();
        if(lens==0)
            return ans;
        int index=lens-1;
        while(nums[index]>=target && index>0)
        {
            index/=2;
        }
        for(int i=index;i<lens;i++)
        {
            if(nums[i]==target)
                ans++;
            else if(nums[i]>target)
                break;
        }
        return ans;
    }
};
