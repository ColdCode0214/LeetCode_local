class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(0, m-2):
            for j in range(0, n-2):
                temp = grid[i][j]+grid[i][j+1]+grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                ans = max(temp, ans)
        return ans