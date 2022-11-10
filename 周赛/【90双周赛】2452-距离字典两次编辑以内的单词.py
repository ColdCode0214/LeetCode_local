class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n1, n2 = len(queries), len(dictionary)
        ans = list()
        for i in range(n1):
            for j in range(n2):
                if len(queries[i]) == len(dictionary[j]):
                    n = len(queries[i])
                    count = 0
                    for k in range(n):
                        if queries[i][k] != dictionary[j][k]:
                            count += 1
                        if count > 2:
                            break
                    if count <= 2:
                        ans.append(queries[i])
                        break
        return ans