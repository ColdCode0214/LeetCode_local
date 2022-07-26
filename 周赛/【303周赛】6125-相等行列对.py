class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        g2 = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            temp = list()
            for i in range(n):
                g2[j][i] = grid[i][j]
        #print("g2:", g2)
        for i in range(n):
            r = grid[i][0:n]
            for j in range(n):
                c = g2[j][0:n]
                #print("r:", r, "c:", c)
                if r == c: ans += 1
        return ans