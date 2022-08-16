class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0 for _ in range(n-2)] for _ in range(n-2)]
        print("ans:", ans)
        temp = list()
        for i in range(0,n-2):
            for j in range(0, n-2):
                a = 0
                for p in range(i, i+3):
                    for q in range(j, j+3):
                        a = max(grid[p][q], a)
                ans[i][j] = a
        return ans