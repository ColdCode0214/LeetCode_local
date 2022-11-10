class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        pre = 0
        for i in range(1,n):
            if ord(s[i]) != ord(s[i-1])+1:
                ans = max(ans, i-pre)
                pre = i
        ans = max(ans, n-pre)
        return ans