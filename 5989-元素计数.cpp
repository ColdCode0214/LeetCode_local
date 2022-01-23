class Solution {
public:
    int countElements(vector<int>& nums) {
        int lens=nums.size();
        if(lens<=2)
            return 0;
        sort(nums.begin(), nums.end());
        int ans=0;
        int l=nums[0], r=nums[lens-1];
        for(int i=0;i<lens;i++)
        {
            if(nums[i]>l && nums[i]<r)
                ans++;
        }
        return ans;
    }
};
