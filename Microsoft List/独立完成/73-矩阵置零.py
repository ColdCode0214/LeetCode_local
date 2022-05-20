class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        queue = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
        # int lens = len(queue)
        # for k in range(lens):
        while(len(queue)>0):
            i, j = queue.pop()
            for p in range(n):
                matrix[i][p] = 0
            for q in range(m):
                matrix[q][j] = 0
