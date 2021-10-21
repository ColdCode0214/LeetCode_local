class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        res = 0
        for i in range(len(nums)):
            res += nums[i]-min_num
        return res