class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        if(startFuel>=target)
            return 0;//�����ʼʱȼ���㹻�࣬����Ҫ����
        int lens=stations.size();//һ����lens������վ

        if(startFuel<target && lens==0)
            return -1;//�����ʼʱȼ�ϲ����ࡢ·��û�м���վ����һ��������Ŀ�ĵ�
        long long int dp[lens+1];//��dp[i]Ϊ��i�������ߵ���Զ�ľ��룬���ʹ������Ϊ����վ�Ĵ���+���
        for(int i=0;i<lens+1;i++)
            dp[i]=0;
        dp[0]=startFuel;
        for(int i=0;i<lens;i++)
        {
            for(int j=i;j>=0;j--)
            {
                if(dp[j]>=stations[i][0])
                    dp[j+1]=max(dp[j+1], dp[j]+stations[i][1]);
            }
        }
        for(int i=0;i<lens+1;i++)
        {
            if(dp[i]>=target)
                return i;
        }
            
        return -1;
    }
};
