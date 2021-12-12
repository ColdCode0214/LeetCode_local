class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int lens=nums.size();
        int l=0, r=0;
        while(r<lens && l<lens)
        {
            if(nums[l]%2==1)
            {
                if(r<l)
                    r=l;
                if(nums[r]%2==1)
                    r++;
                else
                {
                    swap(nums[r], nums[l]);
                    l++;
                }      
            }
            else
                l++;
        }
        vector<int> ans;
        for(int i=0;i<lens;i++)
            ans.push_back(nums[i]);
        return ans;
    }
};
