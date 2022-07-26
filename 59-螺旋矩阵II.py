class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom, left, right = 0, n-1, 0, n-1
        num = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        while num <= n*n:
            i, j = top, left
            while j <= right:
                matrix[i][j] = num
                num += 1
                j += 1
            if num > n*n: break
            top += 1
            i, j = top, right

            while i <= bottom:
                matrix[i][j] = num
                num += 1
                i += 1
            if num > n*n: break
            right -= 1
            i, j = bottom, right

            while j >= left:
                matrix[i][j] = num
                num += 1
                j -= 1
            if num > n*n: break
            bottom -= 1
            i, j = bottom, left

            while i >= top:
                matrix[i][j] = num
                num += 1
                i -= 1
            if num > n*n: break
            left += 1

        return matrix
