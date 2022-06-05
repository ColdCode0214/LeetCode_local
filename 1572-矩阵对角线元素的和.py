class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        lens = len(mat)
        for i in range(lens):
            ans += mat[i][i]
            ans += mat[i][lens - 1 - i]
        if lens % 2 == 1:
            ans -= mat[int(lens / 2)][int(lens / 2)]
        return ans

