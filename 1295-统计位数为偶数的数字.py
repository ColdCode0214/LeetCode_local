class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in nums:
            count = 0
            temp = i
            while i > 0:
                i = int(i/10)
                count += 1
            if count % 2 == 0:
                ans += 1
        return ans