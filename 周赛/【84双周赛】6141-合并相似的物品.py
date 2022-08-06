class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        n1 = len(items1)
        ans = list()
        count = dict()
        for a in items1:
            if a[0] in count:
                count[a[0]] += a[1]
            else:
                count[a[0]] = a[1]
        for a in items2:
            if a[0] in count:
                count[a[0]] += a[1]
            else:
                count[a[0]] = a[1]
        ans = list()
        for a in count.keys():
            ans.append([a, count[a]])
        ans.sort()
        return ans