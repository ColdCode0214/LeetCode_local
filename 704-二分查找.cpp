class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lens=nums.size();
        int left=0, right=lens-1;
        while(left<=right)
        {
            int mid=(right-left)/2+left;
            if(target>nums[mid])
                left=mid+1;
            else if(target<nums[mid])
                right=mid-1;
            else
                return mid;
        }
        return -1;
    }
};
