class Solution:
    def secondHighest(self, s: str) -> int:
        first = sec = -1
        for c in s:
            if c.isdigit():
                d = ord(c)-ord('0')
                if d > first:
                    first, sec = d, first
                elif sec < d < first:
                    sec = d
        return sec