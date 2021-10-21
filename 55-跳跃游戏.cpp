class Solution {
public:
    bool canJump(vector<int>& nums) {
        int lens=nums.size(),maxPos=0, end=0;
        if(lens==1)
            return true;
        for(int i=0;i<lens-1;i++)
        {
            if(maxPos>=i)//表示能到达i
            {
                maxPos=max(maxPos,i+nums[i]);
                if(maxPos>=lens-1)
                    return true;
            }
        }
        return false;
    }
};
