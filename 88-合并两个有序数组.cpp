class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> arr;
        int l=0, r=0;
        while(l<m && r<n)
        {
            if(nums1[l]<nums2[r])
            {
                arr.push_back(nums1[l]);
                l++;
            }
            else
            {
                arr.push_back(nums2[r]);
                r++;
            }
        }
        if(l<m)
        {
            while(l<m)
            {
                arr.push_back(nums1[l]);
                l++;
            }
        }
        if(r<n)
        {
            while(r<n)
            {
                arr.push_back(nums2[r]);
                r++;
            }
        }
        for(int i=0;i<m+n;i++)
            nums1[i]=arr[i];
    }
};
