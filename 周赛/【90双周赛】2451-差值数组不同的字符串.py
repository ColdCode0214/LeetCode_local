class Solution:
    def oddString(self, words: List[str]) -> str:
        lens = len(words)
        n = len(words[0])
        res, cp = list(), list()
        for i in range(lens):
            temp = list()
            for j in range(1, n):
                temp.append(ord(words[i][j]) - ord(words[i][j - 1]))
            res.append(temp)
            cp.append(temp)
        # print("res:", res)
        # cp = res
        cp.sort()
        # print("res:", res)
        # print("cp:", cp)
        if cp[0] == cp[1]:
            tar = cp[len(cp) - 1]
        else:
            tar = cp[0]
        # print("tar:", tar)
        for i in range(len(res)):
            if res[i] == tar:
                index = i
                break
        # print("index:", index)
        return words[i]


