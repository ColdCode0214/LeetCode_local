class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = dict()
        for i in range(len(s)):
            if s[i] not in mp.keys():
                if t[i] in mp.values():
                    return False
                else:
                    mp[s[i]] = t[i]
            else:
                if t[i] != mp[s[i]]:
                    return False
        return True