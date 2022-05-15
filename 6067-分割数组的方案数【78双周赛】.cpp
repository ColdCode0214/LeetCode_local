class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        int lens=nums.size();
        if(lens<=1)
            return 0;
        long long int sum=0;
        for(int i=0;i<lens;i++)
            sum+=nums[i];
        int ans=0;
        long long int l=0, r=sum-l;
        for(int i=0;i<lens-1;i++)
        {
            l+=nums[i];
            r=sum-l;
            if(l>=r)
                ans++;
        }
        return ans;
    }
};
