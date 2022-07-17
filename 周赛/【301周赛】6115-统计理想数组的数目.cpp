class Solution {
//定义两个固定变量
const int MOD = 1000000007;
const int MAXP = 16;
public:  
    int idealArrays(int n, int maxValue) {
        //计算因数
        vector<vector<int>> fac(maxValue+1);
        for(int i=1;i<=maxValue;i++)
            for(int j=i<<1;j<=maxValue;j+=i)
                fac[j].push_back(i);

        //计算子问题的答案
        vector<vector<long long>> f;
        f.resize(maxValue+1, vector<long long>(20));
        for(int i=1;i<=maxValue;i++)
        {
            f[i][1] = 1;
            for(int j=2;j<MAXP;j++)
            {
                for(int t:fac[i])
                {
                    f[i][j] = (f[i][j]+f[t][j-1])%MOD;
                }
            }
        }

        //计算组合数
        vector<vector<long long>> C;
        C.resize(n+1, vector<long long>(20));
        C[0][0]=C[1][0]=C[1][1]=1;
        for(int i=2;i<=n;i++)
        {
            C[i][0]=1;
            for(int j=1;j<=i&&j<=MAXP;j++)
                C[i][j] = (C[i-1][j]+C[i-1][j-1])%MOD;
        }

        //计算最终答案
        long long ans = 0;
        for(int i=1;i<=maxValue;i++)
        {
            for(int j=1;j<=MAXP;j++)
            {
                ans = (ans + C[n-1][j-1]*f[i][j])%MOD;
            }
        }
        return ans;
    }
};
