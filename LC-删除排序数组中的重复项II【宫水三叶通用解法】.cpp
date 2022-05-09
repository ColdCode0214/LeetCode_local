class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        return help(nums, 2);
    }
    int help(vector<int>& nums, int k)
    {
        int lens=0;
        for(auto n:nums)
        {
            if(lens<k || nums[lens-k]!=n)
            {
                nums[lens++]=n;//该语句是先执行对于nums[lens]的赋值，再将lens++
                //lens++;如果将lens++单独提出来进行操作，时间复杂度较高
            }
                
        }
        return lens;
    }
};
