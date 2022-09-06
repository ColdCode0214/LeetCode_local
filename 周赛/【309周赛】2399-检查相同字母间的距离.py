class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        n = len(s)
        mp = dict()
        for i in range(n):
            if s[i] in mp:
                if i-mp[s[i]]-1 != distance[ord(s[i])-97]:
                    return False
            else:
                mp[s[i]] = i
        return True