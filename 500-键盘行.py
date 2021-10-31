class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        hash_map = '12210111011122000010020202'
        ans = []
        for word in words:
            idx = hash_map[ord(word[0].lower())-ord('a')]
            if all(hash_map[ord(w.lower())-ord('a')] == idx for w in word):
                ans.append(word)
        return ans