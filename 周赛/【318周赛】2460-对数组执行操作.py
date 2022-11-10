class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = list()
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i], nums[i+1] = 2*nums[i], 0
            if nums[i] != 0:
                ans.append(nums[i])
        ans.append(nums[n-1])
        ans.extend([0]*(n-len(ans)))
        return ans