class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        if n == 1:
            return 1
        ans = ""
        index = 0
        for i in range(n - 1, -1, -1):
            s2 = int(s[i] + ans, 2)
            print("s2:", s2)
            if s2 <= k:
                ans = s[i] + ans
            else:
                index = i
                break
        print(ans)
        lens = len(ans)
        for i in range(index):
            if s[i] == "0":
                lens += 1
        return lens
