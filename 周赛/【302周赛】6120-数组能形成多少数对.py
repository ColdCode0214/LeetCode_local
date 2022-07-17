class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [0, 1]
        nums.sort()
        print(nums)
        # a, b = 0, n
        mp = dict()
        # for i in range(n):
        #     if nums
        for a in nums:
            if a in mp.keys():
                mp[a] += 1
            else:
                mp[a] = 1
        x, y = 0, 0
        for a in mp.keys():
            x += int(mp[a] / 2)
        y = n - x * 2
        return [x, y]
