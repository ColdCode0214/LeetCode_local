class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        nums.sort()
        nums.reverse()
        for i in range(1,n+1):
            if nums[i-1] >= i and (i == n or nums[i] < i):
                return i
        return ans