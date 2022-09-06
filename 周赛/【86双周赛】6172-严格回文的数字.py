class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        tar = n-2
        cur = 2
        while cur <= tar:
            arr = list()
            cp = n
            while cp > 0:
                arr.append(cp%cur)
                cp = int(cp/cur)
            temp = arr.reverse()
            if temp != arr: return False
            cur += 1
        return True