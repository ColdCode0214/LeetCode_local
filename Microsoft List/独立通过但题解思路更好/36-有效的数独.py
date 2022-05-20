class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            num = [0]*9
            for j in range(9):
                if board[i][j] != '.':
                    num[int(board[i][j])-1] += 1
                    if num[int(board[i][j])-1] > 1:
                        return False
        for j in range(9):
            num = [0]*9
            for i in range(9):
                if board[i][j] != '.':
                    num[int(board[i][j])-1] += 1
                    if num[int(board[i][j])-1] > 1:
                        return False
        x, y = [0, 3, 6], [0, 3, 6]
        for i in x:
            for j in y:
                num = [0]*9
                for p in range(3):
                    for q in range(3):
                        if board[i+p][j+q] != '.':
                            num[int(board[i+p][j+q])-1] += 1
                            if num[int(board[i+p][j+q])-1] > 1:
                                return False
        return True
