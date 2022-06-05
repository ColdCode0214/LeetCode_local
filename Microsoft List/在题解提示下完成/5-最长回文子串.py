class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def dp(i, j) -> bool:
            if i > j: return False
            elif i == j: return True
            elif i+1 == j:
                if s[i] == s[j]:
                    return True
                else: return False
            else:
                if s[i] == s[j] and dp(i+1, j-1) == True:
                    return True
                else: return False
        a = [[False for _ in range(n)] for _ in range(n)]
        size = 0
        ans = ""
        i, j = 0, 0
        gap = 0
        while gap < n:
            for i in range(n-gap):
                j = i + gap
                # if i == j: a[i][j] = True
                # elif i+1 == j:
                #     if s[i] == s[j]: a[i][j] = True
                # else:
                #     if s[i] == s[j] and dp[i+1][j-1] == True: a[i][j] = True
                if s[i] != s[j]:
                    a[i][j] = False
                else:
                    if gap <= 2: a[i][j] = True
                    else: a[i][j] = a[i+1][j-1]
                if a[i][j] == True:
                    if gap+1 > size:
                        size = gap+1
                        ans = s[i:j+1]
            gap += 1

        # for i in range(2, n+1):
        #     #a[i][i] = True
        #     for j in range(n):
        #         a[i][j] = dp(i,j)
        #         #print("a[",i,"][",j,"]:", a[i][j])
        #         if a[i][j] == True:
        #             if j-i+1 > size:
        #                 size = j-i+1
        #                 ans = s[i:j+1]
        return ans