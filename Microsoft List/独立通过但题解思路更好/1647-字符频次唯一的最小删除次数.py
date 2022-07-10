class Solution:
    def minDeletions(self, s: str) -> int:
        mp = dict()
        for a in s:
            if a in mp.keys():
                mp[a] += 1
            else:
                mp[a] = 1
        print(mp)
        ans = 0
        collect = list()
        for a in mp.keys():
            if mp[a] in collect:
                while mp[a] in collect and mp[a] != 0:
                    ans += 1
                    mp[a] -= 1

            collect.append(mp[a])
        return ans
