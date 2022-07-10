class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            if i == 0:
                ans = 1
                lens = 1
            else:
                if nums[i] == nums[i-1] + 1:
                    lens += 1
                elif nums[i] > nums[i-1] + 1:
                    lens = 1
                ans = max(ans, lens)
        return ans
