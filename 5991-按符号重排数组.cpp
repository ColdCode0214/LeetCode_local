class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int lens=nums.size();
        vector<int> ans;
        int p=0, n=0;
        while(p<lens && n<lens)
        {
            if(nums[p]>0 && nums[n]<0)
            {
                ans.push_back(nums[p]);
                ans.push_back(nums[n]);
                p++;
                n++;
            }
            else if(nums[p]<0)
                p++;
            else if(nums[n]>0)
                n++;
        }
        return ans;
    }
};
