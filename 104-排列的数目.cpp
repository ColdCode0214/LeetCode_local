class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        int lens=nums.size();
        if(lens==0)
            return 0;
        int dp[target+1];
        dp[0]=1;
        
        for(int i=1;i<=target;i++)
        {
            dp[i]=0;
            for(int j=0;j<lens;j++)
            {
                if(i>=nums[j] && dp[i-nums[j]]<INT_MAX-dp[i])
                    dp[i]=dp[i]+dp[i-nums[j]];
            }
        }
        /*
        ���ѭ������Ʒ���ڲ�ѭ��������ʱ��ͬ����Ʒ�����������һ�Σ�
        ���ѭ�����������ڲ�ѭ������Ʒʱ��ͬ����Ʒ�Ĳ�ͬ������Ϊ��ͬ���
        for(int i=0;i<=target;i++)
            dp[i]=0;
        dp[0]=1;
        for(int i=0;i<lens;i++)
        {
            for(int j=1;j<=target;j++)
            {
                if(j>=nums[i] && dp[j-nums[i]]<INT_MAX-dp[j])
                    dp[j]=dp[j]+dp[j-nums[i]];
            }
        }
        */

        return dp[target];
    }
};
