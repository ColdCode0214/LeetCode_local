class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> ans;
        int lens=nums.size();
        if(lens<3)
        {
            for(int i=0;i<lens;i++)
                if(ans.size()==0 || nums[i]!=ans[0])
                    ans.push_back(nums[i]);
        }
        else
        {
            sort(nums.begin(),nums.end());
            int unit=lens/3;
            for(int i=unit;i<=lens-1-unit;i++)
            {
                    if((nums[i]==nums[i-unit] || nums[i]==nums[i+unit]) && (ans.size()==0 || nums[i]!=ans[0]))
                        ans.push_back(nums[i]);  
                    if(ans.size()==2)
                        break;
            } 
        }
        return ans;
    }
};
