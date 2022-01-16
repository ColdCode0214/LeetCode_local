class Solution {
public:
    bool isStraight(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int count=0;
        int temp=0;
        for(int i=0;i<5;i++)
        {
            if(nums[i]==0)
                count++;
            else
            {
                if(temp==0)
                    temp=nums[i];
                else
                {
                    if(nums[i]==temp)
                        return false;
                    else if(nums[i]-temp>1)
                        count-=(nums[i]-temp-1);
                    temp=nums[i];
                }
            }
        }
        return count>=0;
    }
};
