class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lens = len(nums)
        if lens == 1:
            return True
        maxPos = nums[0]
        for i in range(1,lens):
            if maxPos >= i:
                maxPos = max(maxPos, nums[i]+i)
                if maxPos >= lens-1:
                    return True
            else:
                return False
        return False
