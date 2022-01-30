class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = Counter(s1.split()) + Counter(s2.split())
        ans = list()
        for word, occ in freq.items():
            if occ == 1:
                ans.append(word)
        return ans