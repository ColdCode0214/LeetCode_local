class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        sm = list()
        sm.append(0)
        for i in range(n):
            sm.append(sm[len(sm) - 1] + nums[i])

        j = 1
        for i in range(1, n + 1, 1):
            while j <= i and (sm[i] - sm[j - 1]) * (i - j + 1) >= k:
                j += 1
            ans += i - j + 1
        return ans