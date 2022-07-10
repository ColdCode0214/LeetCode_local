class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                print("s[i:j]:", s[i:j])
                if dp[i] == True and (s[i:j] in wordDict):
                    dp[j] = True
        print(dp)
        return dp[n]

