class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = dict()
        n2 = len(roads)
        for i in range(n2):
            if roads[i][0] not in count:
                count[roads[i][0]] = 1
            else:
                count[roads[i][0]] += 1
            if roads[i][1] not in count:
                count[roads[i][1]] = 1
            else:
                count[roads[i][1]] += 1
        c = Counter(count).most_common()
        # print(count)
        # print(c)
        # print(type(c))
        # print(len(count))
        num = len(count)
        ans = 0
        for (x,y) in c:
            # print(x,y)
            ans += y*n
            n -= 1
        # while n > 0:
        #     ans += n
        #     n -= 1
        return ans