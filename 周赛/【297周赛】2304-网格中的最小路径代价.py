class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # dp = list()
        # dpr = list()
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = grid[i][j]  # 第一行的代价就是节点的价值
                else:
                    sum = list()
                    for k in range(n):
                        sum.append(dp[i - 1][k] + moveCost[grid[i - 1][k]][j])
                    dp[i][j] = grid[i][j] + min(sum)
        # print(dp)
        return min(dp[m - 1])
