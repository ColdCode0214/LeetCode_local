class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for a in nums:
            if count[a]>1:
                return a