class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s2, t2 = list(), list()
        for a in s:
            if a == '#':
                if len(s2) != 0:
                    s2.pop()
            else:
                s2.append(a)
        for a in t:
            if a == '#':
                if len(t2) != 0:
                    t2.pop()
            else:
                t2.append(a)
        return s2 == t2
