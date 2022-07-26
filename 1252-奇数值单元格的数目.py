class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        lens = len(indices)
        nums = [[0 for _ in range(n)] for _ in range(m)]
        for k in range(lens):
            for j in range(n):
                nums[indices[k][0]][j] += 1
            for i in range(m):
                nums[i][indices[k][1]] += 1
        print(nums)
        ans = 0
        for i in range(m):
            for j in range(n):
                if nums[i][j] % 2 == 1:
                    ans += 1
        return ans