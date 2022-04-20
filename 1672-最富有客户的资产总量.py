import numpy as np
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0])
        sum = []
        ans = 0
        for i in range(m):
            sum.append(0)
            for j in range(n):
                sum[i]+=accounts[i][j]
            ans = max(ans, sum[i])
        return ans
