class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int lens1=nums1.size();
        int lens2=nums2.size();
        vector<int> ans;
        for(int i=0;i<lens1;i++)
        {
            for(int j=0;j<lens2;j++)
            {
                if(nums1[i]==nums2[j])
                {
                    int flag=0;
                    for(int k=0;k<ans.size();k++)
                    {
                        if(ans[k]==nums1[i])
                        {
                            flag=1;
                            break;
                        }
                    }
                    if(flag==0)
                        ans.push_back(nums1[i]);
                }
                    
            }
        }
        return ans;
    }
};
