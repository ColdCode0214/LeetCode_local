class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(ch: str) -> bool:
            return ch in "aeiouAEIOU"

        n = len(s)
        s = list(s)
        l, r = 0, n - 1

        while l < r:
            if (isVowel(s[l])) and (isVowel(s[r])):
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            if not isVowel(s[l]):
                l += 1

            if not isVowel(s[r]):
                r -= 1

        return "".join(s)