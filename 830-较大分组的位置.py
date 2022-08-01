class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = list()
        n = len(s)
        if n < 3: return ans
        l, r = 0, 0
        while l < n and r < n:
            if s[l] == s[r]:
                r += 1
            else:
                if r-l >= 3:
                    ans.append([l, r-1])
                l, r = r, r+1
        if r-l >= 3:
            ans.append([l, r-1])
        return ans