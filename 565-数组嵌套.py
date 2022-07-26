class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        vis = [False] * n
        for i in range(n):
            cnt = 0
            while not vis[i]:
                vis[i] = True
                i = nums[i]
                cnt += 1
            ans = max(ans, cnt)
        return ans