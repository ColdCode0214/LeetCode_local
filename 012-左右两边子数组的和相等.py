class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)

        for i in range(len(nums)):
            r -= nums[i]
            if i > 0:
                l += nums[i-1]
            if l == r:
                return i
        return -1
