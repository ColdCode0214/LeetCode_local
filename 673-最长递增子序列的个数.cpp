class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int lens=nums.size();
        int f[lens], g[lens];
        //定义f[i]为以nums[i]为结尾的最长上升子序列的长度，初始化为1
        //定义g[i]为以nums[i]为结尾的最长上升子序列的数量，初始化为1
        for(int i=0;i<lens;i++)
        {
            f[i]=1;
            g[i]=1;
        }
        int maxtemp=1; //用于记录全局最长递增子序列，初始化为1因为数组中每个元素自己就是一个子序列，也是最长的，长度为1，所以最长子序列长度至少为1
        for(int i=1;i<lens;i++)
        {
            for(int j=0;j<i;j++)
            {
                if(nums[j]<nums[i])
                {
                    if(f[j]+1>f[i])
                    {
                        f[i]=f[j]+1;
                        g[i]=g[j];
                        maxtemp=max(maxtemp,f[i]);
                    }
                    else if(f[j]+1==f[i])
                        g[i]+=g[j];
                }
            }
        }
        int count=0;
        for(int i=0;i<lens;i++)
        {
            if(f[i]==maxtemp)
                count+=g[i];
        }
        return count;
    }
};
