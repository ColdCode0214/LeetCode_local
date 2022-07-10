class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        index1, index2 = list(), list()

        n = len(words)
        ans = n
        l, r = 0, 0
        i1, i2 = -1, -1
        for i in range(n):
            if words[i] == word1:
                i1 = i
                # index1.append(i)
            if words[i] == word2:
                i2 = i
                # index2.append(i)
            if i1 != -1 and i2 != -1:
                ans = min(ans, abs(i1 - i2))
        return ans
