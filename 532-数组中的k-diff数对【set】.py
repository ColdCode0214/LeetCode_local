class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        visited, res = set(), set()
        #n = len(nums)
        for num in nums:
            if num - k in visited:
                res.add(num- k)
            if num + k in visited:
                res.add(num)
            visited.add(num)
        return len(res)