class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        lens = len(nums)
        ans=0
        for i in range(lens-1):
            for j in range(i+1, lens):
                if nums[i] == nums[j]:
                    ans += 1
        return ans