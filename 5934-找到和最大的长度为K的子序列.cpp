class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        int lens=nums.size();
        int copy[lens];
        for(int i=0;i<lens;i++)
            copy[i]=nums[i];
        sort(nums.begin(), nums.end());
        vector<int> ans;
        int flag[k];
        vector<int> temp;
        for(int i=lens-1;i>lens-1-k;i--)
            temp.push_back(nums[i]);
        for(int i=0;i<k;i++)
            flag[i]=0;
        for(int i=0;i<lens;i++)
        {
            for(int j=0;j<k;j++)
            {
                if(copy[i]==temp[j] && flag[j]==0)
                {
                    flag[j]=1;
                    ans.push_back(copy[i]);
                    break;
                }
            }
        }
        return ans;
    }
};
