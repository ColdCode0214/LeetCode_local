class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        for i in range(n):
            ans += max(grid[i])
            for j in range(n):
                if grid[i][j] != 0:
                    ans += 1
        for j in range(n):
            temp = 0
            for i in range(n):
                temp = max(temp, grid[i][j])
            ans += temp
        return ans
