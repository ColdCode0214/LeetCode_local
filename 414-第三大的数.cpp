class Solution {
public:
    int thirdMax(vector<int>& nums) {
        int lens=nums.size();
        int count=1;
        sort(nums.begin(),nums.end());
        int ans=nums[lens-1];
        for(int i=lens-1;i>=0;i--)
        {
            if(nums[i]<ans)
            {
                ans=nums[i];
                count++;
                if(count==3)
                    return ans;
            }
        }
        return nums[lens-1];
    }
};
