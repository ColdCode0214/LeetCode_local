class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        if m==1 and n==1:
            return 0
        ans = 0
        for j in range(n):
            for i in range(m-1):
                if strs[i][j]>strs[i+1][j]:
                    ans += 1
                    break
        return ans