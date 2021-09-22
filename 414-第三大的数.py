class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        lens = len(nums)
        nums.sort()
        count = 1
        ans = nums[lens-1]
        for i in range(lens-1,-1,-1):
            if ans > nums[i]:
                ans = nums[i]
                count+=1
                if count == 3:
                    return ans;
        return nums[lens-1]