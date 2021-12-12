class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        vector<int> ans;
        int lens=nums.size();
        int odd=1, even=0;
        while(odd<lens && even<lens)
        {
            if(nums[odd]%2!=1)
            {
                if(nums[even]%2!=0)
                {
                    swap(nums[odd], nums[even]);
                    odd+=2;
                    even+=2;
                }
                else
                    even+=2;
            }
            else
            {
                odd+=2;
            }
        }
        for(int i=0;i<lens;i++)
            ans.push_back(nums[i]);
        return ans;
    }
};
