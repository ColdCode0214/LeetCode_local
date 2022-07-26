class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count = dict()
        for a in s:
            if a in count.keys():
                return a
            else:
                count[a] = 1
