class Solution {
public:
    int minimumSum(int num) {
        vector<int> nums;
        for(int i=0;i<4;i++)
        {
            nums.push_back(num%10);
            num/=10;
        }
        int ans=0;
        sort(nums.begin(), nums.end());
        int n1=0, n2=0;
        if(nums[0]==0)
        {
            if(nums[1]==0)
            {
                n1=nums[2];
                n2=nums[3];
            }
            else
            {
                n1=nums[1]*10+nums[3];
                n2=nums[2];
            }
        }
        else
        {
            n1=nums[0]*10+nums[3];
            n2=nums[1]*10+nums[2];
        }
        ans=n1+n2;
        return ans;
    }
};
