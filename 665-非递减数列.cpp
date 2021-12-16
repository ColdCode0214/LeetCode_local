class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int count=0;
        int lens=nums.size();
        int temp=0;
        if(lens==1)
            return true;
        for(int i=0;i<lens-1;i++)
        {
            if(nums[i]>nums[i+1])
            {
                count++;
                if(count>=2)
                    return false;
                temp=nums[i];
                nums[i]=nums[i+1];
                if(is_sorted(nums.begin(), nums.end()))
                    return true;
                nums[i]=temp;
                nums[i+1]=nums[i];//对于每个逆序的数对，都有两种修改方式，一种是将前一个的值改为后一个，另一种是将后一个的值改为前一个
                if(is_sorted(nums.begin(), nums.end()))
                    return true;
            }
        }
        return true;
    }
};
