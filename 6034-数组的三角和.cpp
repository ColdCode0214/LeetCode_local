class Solution {
public:
    int triangularSum(vector<int>& nums) {
        int lens=nums.size();
        vector<int> n1;
        vector<int> n2;
        int ans=0;
        for(int i=0;i<lens;i++)
        {
            n1.push_back(nums[i]);
        }
        while(n1.size()>1)
        {
            for(int i=0;i<n1.size()-1;i++)
            {
                n2.push_back((n1[i]+n1[i+1])%10);
            }
            n1.clear();
            n1=n2;
            n2.clear();
        }
        ans=n1[0];
        return ans;
    }
};
