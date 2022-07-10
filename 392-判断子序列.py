class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si, ti = 0, 0
        ns, nt = len(s), len(t)
        if ns == 0: return True
        while si < ns and ti < nt:
            if s[si] == t[ti]:
                si += 1
                if si == ns:
                    return True
            ti += 1
        return False