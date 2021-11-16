class Solution:
    def jump(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens == 1:
            return 0
        steps = 0
        end = 0
        maxPos = 0
        for i in range(lens-1):
            maxPos = max(maxPos, nums[i]+i)
            if i == end:
                steps = steps+1
                end = maxPos
        return steps
