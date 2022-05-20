class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0] * 10 for _ in range(9)]
        column = [[0] * 10 for _ in range(9)]
        boxNum = [[0] * 10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                curNum = int(board[i][j])
                row[i][curNum] += 1
                column[j][curNum] += 1
                boxNum[j//3+(i//3)*3][curNum] += 1
                if row[i][curNum] > 1:
                    return False
                if column[j][curNum] > 1:
                    return False
                if boxNum[j//3 + i // 3 * 3][curNum] > 1:
                    return False
        return True