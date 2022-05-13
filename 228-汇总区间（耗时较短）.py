class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        a = []
        x = 0
        y = 0
        while x != len(nums):
            if x+1 < len(nums) and nums[x]+1 == nums[x+1]:
                x += 1
            else:
                if x -y != 0:
                    a.append("{}->{}".format(nums[y],nums[x]))
                else:
                    a.append("{}".format(nums[x]))
                x += 1
                y = x
        return a
