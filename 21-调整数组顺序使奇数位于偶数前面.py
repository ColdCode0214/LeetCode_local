class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        lens = len(nums)
        left, right = 0, lens-1
        while left < right:
            if nums[left] % 2 == 0 and nums[right] % 2 == 1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] % 2 != 0:
                left += 1
            elif nums[right] % 2 != 1:
                right -= 1
        return nums