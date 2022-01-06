class Solution:
    def compressString(self, S: str) -> str:
        n = len(S)
        if n == 0:
            return S
        res = ''
        res += S[0]
        index = 0
        for i in range(n):
            if S[i] != res[len(res)-1]:
                res += str(i - index)
                res += S[i]
                index = i
            if i == n-1:
                res += str(n-1 - index + 1)
        return res if len(res) < len(S) else S