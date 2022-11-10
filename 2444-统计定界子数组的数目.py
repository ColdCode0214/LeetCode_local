class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        l, r1, r2, ans = -1, -1, -1, 0
        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                l = i
            if nums[i] == minK:
                r1 = i
            if nums[i] == maxK:
                r2 = i
            ans += max(0, min(r1, r2)-l)
        return ans