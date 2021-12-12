class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {
        int lens=nums.size();
        long long int sum=0;
        long long int big=0, small=0;
        for(int i=0;i<lens-1;i++)
        {
            big=nums[i], small=nums[i];
            for(int j=i+1;j<lens;j++)
            {
                if(nums[j]>big)
                    big=nums[j];
                if(nums[j]<small)
                    small=nums[j];
                sum+=(big-small);
            }
        }
        return sum;
    }
};
