class Solution {
public:
    int jump(vector<int>& nums) {
        int lens=nums.size();
        int end=0;
        int maxPos=0;
        int step=0;
        for(int i=0;i<lens-1;i++)
        {
                maxPos=max(maxPos, i+nums[i]);
                if(i==end)
                {
                    end = maxPos;
                    step++;
                }
        }
        return step;
    }
};
