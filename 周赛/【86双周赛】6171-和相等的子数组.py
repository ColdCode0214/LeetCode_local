class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        mp = dict()
        for i in range(n-1):
            if nums[i]+nums[i+1] in mp:
                mp[nums[i]+nums[i+1]] += 1
            else:
                mp[nums[i]+nums[i+1]] = 1
        for a in mp.keys():
            if mp[a] > 1:
                return True
        return False