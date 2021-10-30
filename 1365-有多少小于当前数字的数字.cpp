class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int lens=nums.size();
        vector<int> ans;
        int count=0;
        for(int i=0;i<lens;i++)
        {
            count=0;
            for(int j=0;j<lens;j++)
            {
                if(i!=j && nums[j]<nums[i])
                    count++;
            }
            ans.push_back(count);
        }
        return ans;
    }
};
