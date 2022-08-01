class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        temp = 0
        nums.sort()
        while nums[n - 1] > 0:
            temp = 0
            for i in range(n):
                if nums[i] != 0 and temp == 0:
                    temp = nums[i]
                    # break
                if temp != 0:
                    nums[i] -= temp
            nums.sort()
            ans += 1
        return ans
        # for i in range(n):

