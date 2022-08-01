class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        lens = len(pattern)
        n = len(words)
        ans = list()
        for i in range(n):
            p2w, w2p = dict(), dict()
            flag = 0
            for k in range(lens):
                if words[i][k] in w2p:
                    if w2p[words[i][k]] != pattern[k]:
                        flag = 1
                        break
                else:
                    w2p[words[i][k]] = pattern[k]
                if pattern[k] in p2w:
                    if p2w[pattern[k]] != words[i][k]:
                        flag = 1
                        break
                else:
                    p2w[pattern[k]] = words[i][k]
            if flag == 0:
                ans.append(words[i])
        return ans