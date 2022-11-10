class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        n = len(nums)
        for a in nums:
            if a % 2 == 0 and a % 3 == 0:
                ans += a
                count += 1
        if count == 0:
            return 0
        else:
            return int(ans/count)