class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        p1, p2 = 0, 0
        ans = ''
        while p1 < l1 and p2 < l2:
            ans += (word1[p1] + word2[p2])
            p1 += 1
            p2 += 1
        while p1 < l1:
            ans += word1[p1]
            p1 += 1
        while p2 < l2:
            ans += word2[p2]
            p2 += 1
        return ans
