class Solution {
public:
    bool divideArray(vector<int>& nums) {
        int lens=nums.size();
        sort(nums.begin(), nums.end());
        for(int i=0;i<lens;i+=2)
        {
            if(nums[i]!=nums[i+1])
                return false;
        }
        return true;
    }
};
