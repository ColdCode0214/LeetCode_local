class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # if n == 1: return 0
        # nums.sort()
        # if nums[n-1]-nums[0] <= 2*k: return 0
        # else:
        #     return nums[n-1]-nums[0] - 2*k

        # if max(nums)-min(nums) <= 2*k: return 0
        # else: return max(nums)-min(nums) - 2*k

        #return max(0, max(nums)-min(nums) - 2*k)

        gap = max(nums) - min(nums)
        if gap <= 2*k:
            return 0
        else:
            return gap-2*k