class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isLetter(ch: str) -> bool:
            return ch in "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        n = len(s)
        l, r = 0, n-1
        while l < r:
            if isLetter(s[l]) and isLetter(s[r]):
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            if not isLetter(s[l]):
                l += 1
            if not isLetter(s[r]):
                r -= 1
        return True