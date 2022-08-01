class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = dict()
        n = len(s)
        ans = list()
        if n < 10: return ans
        for i in range(n-9):
            if s[i:i+10] in mp:
                mp[s[i:i+10]] += 1
            else:
                mp[s[i:i+10]] = 1
        for a in mp.keys():
            if mp[a] > 1:
                ans.append(a)
        return ans