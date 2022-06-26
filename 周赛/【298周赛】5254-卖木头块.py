class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        lens = len(prices)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(lens):
            hi, wi, pi = prices[i][0], prices[i][1], prices[i][2]
            dp[hi][wi] = pi
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(1, i):
                    dp[i][j] = max(dp[i][j], dp[k][j]+dp[i-k][j])
                for k in range(1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[i][j-k])
        return dp[m][n]