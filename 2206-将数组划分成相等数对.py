class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        for a in count.values():
            if a%2 == 1:
                return False
        return True