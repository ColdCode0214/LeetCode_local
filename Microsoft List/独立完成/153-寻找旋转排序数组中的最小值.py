class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0, n-1
        if nums[l] < nums[r]: return nums[l]
        while l < r:
            mid = int((l+r)/2)
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[l]:
                l = mid
            else:
                return nums[l+1]
        return nums[l+1]