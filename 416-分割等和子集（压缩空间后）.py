class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = int(sum(nums)/2)
        dp = [False for _ in range(target +1)]
        for i in range(len(nums)):
            for j in range(target, -1, -1):
                if nums[i] > j:
                    break
                elif nums[i] == j:
                    dp[j] = True
                else:
                    dp[j] = dp[j] or dp[j-nums[i]]
                if dp[target] == True:
                    return True
        return False