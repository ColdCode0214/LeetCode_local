class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        int lens=nums.size();
        int ans=0;
        for(int i=0;i<lens-1;i++)
        {
            for(int j=i+1;j<lens;j++)
            {
                if(nums[i]==nums[j] && (i*j)%k==0)
                    ans++;
            }
        }
        return ans;
    }
};
