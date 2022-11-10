class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        mp = dict()
        for a in nums:
            if a % space in mp:
                mp[a % space].append(a)
            else:
                mp[a % space] = [a]
        ans, max_ = 0, 0
        for a in mp:
            if len(mp[a]) > max_:
                max_ = len(mp[a])
                ans = min(mp[a])
            elif len(mp[a]) == max_:
                if min(mp[a]) < ans:
                    ans = min(mp[a])
        return ans