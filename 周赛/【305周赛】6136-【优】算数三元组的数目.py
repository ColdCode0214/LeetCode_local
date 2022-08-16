class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i]-diff in nums and nums[i]+diff in nums:
                ans += 1
        return ans