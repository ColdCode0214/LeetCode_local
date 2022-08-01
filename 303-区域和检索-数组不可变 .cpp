class NumArray {
public:

    vector<int> nums2;

    NumArray(vector<int>& nums) {
        nums2=nums;
        int n=nums.size();
        for(int i=1;i<n;i++)
            nums2[i]+=nums2[i-1];

    }
    
    int sumRange(int left, int right) {
        if(left==0)
            return nums2[right];
        else
            return nums2[right]-nums2[left-1];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
