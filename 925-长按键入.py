class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def compressString(S: str) -> str:
            n = len(S)
            if n == 0:
                return S
            res = ''
            sum = []
            res += S[0]
            index = 0
            for i in range(n):
                if S[i] != res[len(res)-1]:
                    sum.append(i-index)
                    res += S[i]
                    index = i
                if i == n-1:
                    sum.append(n-1 - index + 1)
            return res, sum
        str1, sum1 = compressString(name)
        str2, sum2 = compressString(typed)
        if len(str1) != len(str2):
            return False
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
            if sum1[i] > sum2[i]:
                return False
        return True