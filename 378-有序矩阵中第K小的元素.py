class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # n = len(matrix)
        # tran = list()
        # for i in range(n):
        #     tran.extend(matrix[i])
        # tran.sort()
        # return tran[k-1]
        # 二分法
        n = len(matrix)
        def check(mid):
            i, j = n-1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i+1
                    j += 1
                else:
                    i -= 1
            return num >= k
        l, r = matrix[0][0], matrix[n-1][n-1]
        while l < r:
            mid = (l+r)//2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l