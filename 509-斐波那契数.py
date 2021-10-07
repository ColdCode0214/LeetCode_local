class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        ans = [0 for i in range(n+1)]
        ans[0]=0
        ans[1]=1
        for i in range(2,n+1):
            ans[i]=ans[i-1]+ans[i-2]
        return ans[n]