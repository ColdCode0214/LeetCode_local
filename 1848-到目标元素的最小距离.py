class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        index = list()
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                index.append(abs(i-start))
        return min(index)