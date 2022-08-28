class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        ans = 0
        m, p, g = 0, 0, 0
        for i in range(n):
            if 'M' in garbage[i]:
                m = i
            if 'P' in garbage[i]:
                p = i
            if 'G' in garbage[i]:
                g = i
        for i in range(n):
            ans += len(garbage[i])
            if i <= m and i > 0:
                ans += travel[i - 1]
            if i <= p and i > 0:
                ans += travel[i - 1]
            if i <= g and i > 0:
                ans += travel[i - 1]
        return ans


