class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 实现原地修改矩阵完成本题
        # 将死而复生的细胞标记为“-1”，表示该细胞是活的但之前是死的
        # 将新死亡的细胞标记为“2”，表示该细胞是死的但之前是活的
        # 注意新加入的状态（2/-1）要和对应的更新前状态性质相同
        m, n = len(board), len(board[0])
        #ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    count = 0 #记录死细胞周围活细胞的数量
                    for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                        if 0 <= x < m and 0 <= y < n:
                            if board[x][y] >= 1: 
                                count += 1
                    if i == 1 and j == 0:
                        print(board)
                    print("i:", i, "j:", j)
                    print("count:", count)
                    if count == 3: board[i][j] = -1
                    #else: ans[i][j] = 0
                else:
                    count = 0 #记录活细胞周围活细胞的数量
                    for x, y in ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)):
                        if 0 <= x < m and 0 <= y < n:
                            if board[x][y] >= 1: 
                                count += 1
                    if count < 2 or count > 3: board[i][j] = 2
                    #else: board[i][j] = 1
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1: board[i][j] = 1
                if board[i][j] == 2: board[i][j] = 0