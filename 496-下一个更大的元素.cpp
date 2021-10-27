class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int lens1=nums1.size();
        int lens2=nums2.size();
        int flag=0,find=0;
        vector<int> ans;
        for(int i=0;i<lens1;i++)
        {
            flag=0;
            find=0;
            for(int j=0;j<lens2;j++)
            {
                if(nums2[j]==nums1[i])
                    find=1;
                if(nums2[j]>nums1[i] && find==1)
                {
                    flag=1;
                    ans.push_back(nums2[j]);
                    break;
                }
            }
            if(flag==0)
                ans.push_back(-1);
        }
        return ans;
    }
};
