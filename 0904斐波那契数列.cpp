class Solution {
public:
    int fib(int n) {
        if(n==0)
            return 0;
        if(n==1)
            return 1;
        else
        {
            int ans[n+1];
            ans[0]=0,ans[1]=1;
            for(int i=2;i<=n;i++)
            {
                ans[i]=(ans[i-1]+ans[i-2])%1000000007;
            }
            //ans[n]=ans[n]%1000000007;
            return ans[n];
        }
    }
};
