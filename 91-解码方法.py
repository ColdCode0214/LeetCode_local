class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # 给定只包含数字的字符串，将该字符串拆分成若干不大于26的数（不能有前导0），求一共多少种拆分方式
        arr = list()
        for a in s:
            arr.append(int(a))
        # print(arr)
        if arr[0] == 0: return 0
        dp = [0]*n
        dp[0] = 1
        if n == 1: return 1
        if arr[1] != 0: dp[1] += 1
        if arr[0]*10+arr[1] <= 26: dp[1] += 1
        for i in range(2, n):
            if arr[i-1]*10+arr[i] <= 26 and arr[i-1] != 0:
                dp[i] += dp[i-2]
            if arr[i] != 0:
                dp[i] += dp[i-1]
        # print(dp)
        return dp[n-1]