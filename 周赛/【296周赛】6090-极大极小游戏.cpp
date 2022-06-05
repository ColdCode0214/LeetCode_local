class Solution {
public:
    int minMaxGame(vector<int>& nums) {
        int lens=nums.size();
        while(lens>1)
        {
            int newnum[lens/2];
            for(int i=0;i<lens/2;i++)
            {
                if(i%2==0)
                {
                    newnum[i]=min(nums[2 * i], nums[2 * i + 1]);
        
                }
                else
                {
                    newnum[i]=max(nums[2 * i], nums[2 * i + 1]);
                }
            }
            nums.clear();
            for(int i=0;i<lens/2;i++)
            {
                nums.push_back(newnum[i]);
            }
            lens=nums.size();
        }
        return nums[0];
    }
};
