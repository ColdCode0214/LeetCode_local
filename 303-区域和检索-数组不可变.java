class NumArray {
    int[] sums;
    public NumArray(int[] nums) {
        int n=nums.length;
        sums=new int[n+1];
        for(int i=0;i<n;i++)
        {
            sums[i+1]=sums[i]+nums[i];
        }
    }
    
    public int sumRange(int left, int right) {
        return sums[right+1]-sums[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */