class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up, down = 1, 1
        n = len(nums)
        if n == 0: return 0
        for i in range(n-1):
            if nums[i+1] > nums[i]:
                up = down + 1
            elif nums[i+1] < nums[i]:
                down = up + 1
        return max(up, down)