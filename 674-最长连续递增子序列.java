class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int n=nums.length;
        int ans=0;
        int index=0;
        for(int i=1;i<n;i++)
        {
            if(nums[i]<=nums[i-1])
            {
                ans=Math.max(ans, i-index);
                index=i;
            }
        }
        ans=Math.max(ans, n-index);
        return ans;
    }
}