class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 1000000007
        d = abs(endPos - startPos)
        if d > k or (k - d) % 2 == 1: return 0
        f = [[0 for _ in range(k + 1)] for _ in range(k + 1)]
        for i in range(k + 1):
            f[i][0] = 1
            for j in range(1, i + 1):
                f[i][j] = (f[i - 1][j] + f[i - 1][j - 1]) % MOD
                if i == k and j == int((d + k) / 2): return f[i][j]
