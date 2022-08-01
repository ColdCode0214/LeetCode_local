class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # arr = list()
        # for i in range(n):
        #     arr.append(nums[0]+i)
        count = nums[0]+1
        ans = 0
        for i in range(1,n):
            if count <= nums[i]:
                count = nums[i]+1
            else:
                ans += (count-nums[i])
                count += 1
        return ans
