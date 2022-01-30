class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        int lens=nums.size();
        for(int i=0;i<lens;i++)
        {
            if(nums[i]==original)
            {
                original*=2;
                i=-1;
            }
        }
        return original;
    }
};
