class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = list()
        rmin, cmax = list(), list()
        for i in range(m):
            rmin.append(min(matrix[i]))
        print(rmin)
        for j in range(n):
            index = 0
            temp = matrix[0][j]
            print("temp:", temp)
            for i in range(m):
                if matrix[i][j] > temp:
                    temp = matrix[i][j]
                    index = i
            if rmin[index] == temp:
                ans.append(temp)
        return ans