class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        int lens=primes.size();
        int ans[n];
        ans[0]=1;//第一个丑数总是1
        int temp[lens], p[lens];
        for(int i=0;i<lens;i++)
            p[i]=0;
        for(int i=1;i<n;i++)
        {
            ans[i]=2147483647;
            for(int j=0;j<lens;j++)
            {
                temp[j]=ans[p[j]]*primes[j];
                if(temp[j]<ans[i])
                    ans[i]=temp[j];
            }
            /*
            int min=temp[0];
            for(int j=0;j<lens;j++)
                if(temp[j]<min)
                    min=temp[j];
            */
            //ans[i]=min;
            for(int j=0;j<lens;j++)
            {
                if(temp[j]==ans[i])
                    p[j]++;
            }

        }
        return ans[n-1];
    }
};
