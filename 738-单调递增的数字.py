class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        base = 111111111
        ans = 0
        for i in range(9):
            while ans + base > n:
                base //= 10
            ans += base
        return ans