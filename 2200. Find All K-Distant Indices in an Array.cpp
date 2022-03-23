class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        vector<int> ans;
        int lens=nums.size();
        int flag[lens];
        for(int i=0;i<lens;i++)
            flag[i]=0;
        for(int i=0;i<lens;i++)
        {
            for(int j=0;j<lens;j++)
            {
                if(nums[i]==key)
                {
                    if(abs(j-i)<=k && flag[j]==0)
                    {
                        ans.push_back(j);
                        flag[j]=1;
                    }
                        
                    
                }
            }
        }
        /*
        for(int i=0;i<ans.size();i++)
            cout<<ans[i]<<" ";
        sort(ans.begin(), ans.end());
        ans.resize(unique(nums.begin(), nums.end())-nums.begin());*/
        return ans;
    }
};
