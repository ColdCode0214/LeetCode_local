class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i - 1, i - 1 - dp[i - 1], -1):
                # print("nums[i]:", nums[i], "nums[j]:", nums[j])
                if nums[i] & nums[j] != 0:
                    dp[i] = i - j
                    break
                if j == i - 1 - dp[i - 1] + 1:
                    dp[i] = dp[i - 1] + 1
        # print(dp)
        return max(dp)
