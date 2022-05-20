class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 本题相当于求腐烂橘子到新鲜橘子的最短路径，因此不用DFS而使用BFS
        # 先统计最初的新鲜橘子总数，同时将腐烂橘子的坐标加入queue中
        count = 0
        queue = []
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        # 接下来进行BFS，将新鲜橘子变为腐烂橘子
        # def change(grid, m, n, r, c, count):
        #     if 0<=r<m and 0<=c<n:
        #         if grid[r][c] == 1:
        #             count -= 1
        #             queue.append((r,c))
        #             grid[r][c] = 2
        round = 0
        while count > 0 and len(queue) > 0:
            round += 1
            k = len(queue)  # 避免直接把下面新添加的橘子也当成上一批就腐烂的而进行遍历
            for i in range(k):
                r, c = queue.pop(0)
                # change(grid, m, n, r-1, c, count)
                # change(grid, m, n, r+1, c, count)
                # change(grid, m, n, r, c-1, count)
                # change(grid, m, n, r, c+1, count)
                if r - 1 >= 0:
                    if grid[r - 1][c] == 1:
                        count -= 1
                        queue.append((r - 1, c))
                        grid[r - 1][c] = 2
                if r + 1 < m:
                    if grid[r + 1][c] == 1:
                        count -= 1
                        queue.append((r + 1, c))
                        grid[r + 1][c] = 2
                if c - 1 >= 0:
                    if grid[r][c - 1] == 1:
                        count -= 1
                        queue.append((r, c - 1))
                        grid[r][c - 1] = 2
                if c + 1 < n:
                    if grid[r][c + 1] == 1:
                        count -= 1
                        queue.append((r, c + 1))
                        grid[r][c + 1] = 2
        if count > 0:
            return -1
        return round

