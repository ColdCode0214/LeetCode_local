class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        ans = list()
        for i in range(n):
            for j in range(n):
                if i != j and len(words[i]) <= len(words[j]):
                    if words[i] in words[j]:
                        ans.append(words[i])
                        break
        return ans
