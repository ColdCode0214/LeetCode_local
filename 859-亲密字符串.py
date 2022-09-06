class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        ns, ng = len(s), len(goal)
        if ns != ng: return False
        dif = list()
        for i in range(ns):
            if s[i] != goal[i]:
                dif.append(i)
        if len(dif) == 0:
            if len(set(s)) < ns: return True
        if len(dif) == 2:
            if s[dif[0]] == goal[dif[1]] and s[dif[1]] == goal[dif[0]]: return True
        return False

