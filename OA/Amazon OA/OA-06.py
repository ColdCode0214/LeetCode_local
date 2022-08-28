'''
The engineer wants to find the maximum number of times a target word
can be obtained by rearranging a subset of characters in a log entry.
Given a log entry s and target word t, the target word can be obtained
by selecting some subset of characters from s that can be rearranged to
form string t and removing them from s.
Determint the maximum number of times the target word can be removed
from the given log entry.
Note: Both strings s and t consist only of lowercase English letters.
'''

from collections import Counter

s = "abacbc"
t = "bca"

def oa1t6(s: str, t: str):
    counts, countt = Counter(s), Counter(t)
    ans = len(s)
    for a in countt:
        if a not in counts:
            return 0
        ans = min(ans, int(counts[a]/countt[a]))
    return ans

print(oa1t6(s, t))
