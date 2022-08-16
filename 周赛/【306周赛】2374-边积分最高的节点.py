class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        count = dict()
        n = len(edges)
        for i in range(n):
            if edges[i] in count:
                count[edges[i]] += i
            else:
                count[edges[i]] = i
        ans = 0
        temp = 0
        for a in count.keys():
            if count[a] > temp:
                ans = a
                temp = count[a]
            elif count[a] == temp:
                if a < ans:
                    ans = a
        return ans