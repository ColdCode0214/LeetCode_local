class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        temp = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                temp += nums[i]
            else:
                ans = max(temp, ans)
                temp = nums[i]
        ans = max(temp, ans)
        return ans