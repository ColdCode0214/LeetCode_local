class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        m = len(mat)
        for i in range(m):
            if sum(mat[i]) == 1:
                col = mat[i].index(1) # 找出1所在位置的下标
                # print("col:", col)
                if sum(mat[k][col] for k in range(m)) == 1:
                     ans += 1
        return ans