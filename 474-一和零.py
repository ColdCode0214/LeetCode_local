class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        lens = len(strs)
        for k in range(lens):
            ki, kj = strs[k].count('0'), strs[k].count('1')
            #print(dp)
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if ki <= i and kj <= j:
                        dp[i][j] = max(dp[i][j], dp[i-ki][j-kj]+1)
        return dp[m][n]