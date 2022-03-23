class Solution {
public:
    int mostFrequent(vector<int>& nums, int key) {
        int lens=nums.size();
        int ans=0;
        unordered_map<int, int> mp;
        for(int i=0;i<lens-1;i++)
        {
            if(nums[i]==key)
            {
                mp[nums[i+1]]++;
            }
        }
        int temp=0;
        for(auto& a:mp)
        {
            if(a.second>temp)
            {
                temp=a.second;
                ans=a.first;
            }
        }
        return ans;
    }
};
