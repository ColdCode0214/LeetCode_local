class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int lens=nums.size();
        int ans=0;
        for(int i=0;i<lens-1;i++)
        {
            for(int j=i+1;j<lens;j++)
            {
                if(nums[i]==nums[j])
                    ans++;
            }
        }
        return ans;
    }
};
