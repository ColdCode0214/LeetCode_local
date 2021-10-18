class Solution {
public:
    bool divisorGame(int n) {
        if(n==1)
            return false;
        bool f[n+1];//true-先手胜；false-先手败
        for(int i=0;i<n+1;i++)
            f[i]=false;
        f[2]=true;
        for(int i=3;i<=n;i++)
        {
            for(int j=1;j<i;j++)
                if(f[j]==true && i%j==0)
                    f[i]=true;
        }
        return f[n];
    }
};