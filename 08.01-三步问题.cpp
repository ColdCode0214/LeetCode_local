class Solution {
public:
    int waysToStep(int n) {
        if(n==1 || n==2)
            return n;
        long long int ans[n];
        ans[0]=1, ans[1]=2, ans[2]=4;
        for(int i=3;i<n;i++)
            ans[i]=(ans[i-1]%1000000007+ans[i-2]%1000000007+ans[i-3]%1000000007)%1000000007;
        return ans[n-1];
    }
};
