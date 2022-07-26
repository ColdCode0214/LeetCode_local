class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    count = 0 #记录死细胞周围活细胞的数量
                    for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                        if 0 <= x < m and 0 <= y < n:
                            if board[x][y] == 1:
                                count += 1
                    if count == 3: ans[i][j] = 1
                    else: ans[i][j] = 0
                else:
                    count = 0 #记录活细胞周围活细胞的数量
                    for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                        if 0 <= x < m and 0 <= y < n:
                            if board[x][y] == 1:
                                count += 1
                    if count < 2 or count > 3: ans[i][j] = 0
                    else: ans[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = ans[i][j]
