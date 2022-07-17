class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        mp = dict()
        for i in range(n):
            temp = nums[i]
            a = list()
            while temp > 0:
                a.append(temp % 10)
                temp = int(temp / 10)
            sum_a = sum(a)
            if sum_a in mp.keys():
                mp[sum_a].append(nums[i])
            else:
                mp[sum_a] = [nums[i]]
        ans = -1
        for a in mp.keys():
            if len(mp[a]) >= 2:
                mp[a].sort()
                mp[a].reverse()
                k = mp[a][0] + mp[a][1]
                ans = max(ans, k)
        return ans
#         if ans == -1: return -1
#         print(mp)
#         print("ans:", ans)
#         print(mp[ans])
#         mp[ans].sort()
#         mp[ans].reverse()

#         res = nums[mp[ans][0]]+nums[mp[ans][1]]
#         return res