class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int lens=nums.size();
        int flag[lens];
        for(int i=0;i<lens;i++)
            flag[i]=0;
        vector<int> ans;
        for(int i=0;i<lens;i++)
            flag[nums[i]-1]=1;
        for(int i=0;i<lens;i++)
        {
            if(flag[i]==0)
                ans.push_back(i+1);
        }
        return ans;
    }
};
