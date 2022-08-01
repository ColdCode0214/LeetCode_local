class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        done = set()
        ans = -1
        for i in range(n):
            #print("i:", i)
            l = dict()
            count = 0
            if i not in done:
                # print("i:", i)
                # print("ans:", ans)
                node = i
                while node != -1:
                    if node in done:
                        # print("node@:", node)
                        break
                    if node in l:
                        ans = max(ans, count-l[node])
                        break
                    else:
                        l[node] = count
                        #done.add(node)
                        count += 1
                        node = edges[node]
            for a in l.keys():
                done.add(a)
        return ans