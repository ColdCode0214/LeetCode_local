class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        count = 0
        for i in range(len(nums)):
            cur = total - nums[i]
            if 2*count == cur:
                return i
            count += nums[i]
        return -1
