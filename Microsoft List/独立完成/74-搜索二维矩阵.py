class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        u, d, l, r = 0, m-1, 0, n-1
        goal = -1
        while u < d:
            mid = u + int((d-u)/2)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                d = mid-1
            else:
                if matrix[mid][n-1] < target:
                    u = mid+1
                else:
                    goal = mid
                    break
        if goal == -1: goal = u
        print("goal:", goal)
        if n == 1:
            if matrix[goal][0] == target:
                return True
            else:
                return False
        while l <= r:
            mid = int((l+r)/2)
            print("m[goal][mid]:", matrix[goal][mid])
            if matrix[goal][mid] == target:
                return True
            elif matrix[goal][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
