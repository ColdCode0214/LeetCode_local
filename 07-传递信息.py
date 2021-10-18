class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp = [[0]*(n+1) for _ in range(k+1)]
        dp[0][0] = 1
        for i in range(k):
            for edge in relation:
                src, dst = edge[0], edge[1]
                dp[i+1][dst] += dp[i][src]
        return dp[k][n-1]
