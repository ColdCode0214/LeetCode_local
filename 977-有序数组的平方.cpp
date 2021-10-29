class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> ans;
        int lens=nums.size();
        for(int i=0;i<lens;i++)
             ans.push_back(pow(nums[i],2));
        sort(ans.begin(),ans.end());
        return ans;
    }
};
