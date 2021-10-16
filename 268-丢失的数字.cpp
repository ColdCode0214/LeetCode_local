class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int lens=nums.size();
        for(int i=0;i<lens;i++)
        {
            if(nums[i]!=i)
                return i;
        }
        return lens;
    }
};
