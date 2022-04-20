class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int lens=nums.size();
        int m=abs(nums[0]);
        int ans=nums[0];
        for(int i=0;i<lens;i++)
        {

            if(abs(nums[i])<m)
            {
                m=abs(nums[i]);
                ans=nums[i];
            }
            else if(nums[i]==m && nums[i]>ans)
            {
                m=abs(nums[i]);
                ans=nums[i];
            }
        }
        return ans;
    }
};
