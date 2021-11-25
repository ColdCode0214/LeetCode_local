class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        int n=nums.size();
        unordered_map<int, vector<int>> mp;
        for(int i=0;i<n;i++)
        {
            if(mp.count(nums[i]))
            {
                mp[nums[i]][0]++;
                mp[nums[i]][2]=i;
            }
            else
                mp[nums[i]]={1,i,i};
        }
        int maxNum=0, minLen=0;
        for(auto& [_, vec]:mp)
        {
            if(maxNum<vec[0])
            {
                maxNum=vec[0];
                minLen=vec[2]-vec[1]+1;
            }
            else if(maxNum==vec[0])
                if(minLen>vec[2]-vec[1]+1)
                    minLen=vec[2]-vec[1]+1;
        }
        return minLen;
    }
};
