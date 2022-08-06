class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int lens=nums.size();
        int f[lens], g[lens];
        //����f[i]Ϊ��nums[i]Ϊ��β������������еĳ��ȣ���ʼ��Ϊ1
        //����g[i]Ϊ��nums[i]Ϊ��β������������е���������ʼ��Ϊ1
        for(int i=0;i<lens;i++)
        {
            f[i]=1;
            g[i]=1;
        }
        int maxtemp=1; //���ڼ�¼ȫ������������У���ʼ��Ϊ1��Ϊ������ÿ��Ԫ���Լ�����һ�������У�Ҳ����ģ�����Ϊ1������������г�������Ϊ1
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
