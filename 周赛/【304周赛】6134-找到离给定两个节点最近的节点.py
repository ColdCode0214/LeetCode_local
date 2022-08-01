class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        # 分别求出node1和node2能到达的节点以及距离
        l1, l2 = dict(), dict()
        c1, c2 = node1, node2

        # l1[node1] = 0
        # l2[node2] = 0
        # count = 1
        count = 0
        # while edges[node1] != -1:
        #     if edges[node1] in l1: break
        #     else:
        #         l1[edges[node1]] = count
        #         count += 1
        #         node1 = edges[node1]
        while node1 != -1:
            if node1 in l1:
                break
            else:
                l1[node1] = count
                count += 1
                node1 = edges[node1]
        count = 0
        while node2 != -1:
            if node2 in l2:
                break
            else:
                l2[node2] = count
                count += 1
                node2 = edges[node2]
        # print("l1:", l1, "l2:", l2)
        ans = list()
        heapq.heapify(ans)
        for a in l1:
            if a in l2:
                dis = max(l1[a], l2[a])
                heapq.heappush(ans, [dis, a])
        if len(ans) == 0: return -1
        ansnode = heapq.nsmallest(1, ans)
        # print("ansnode:", ansnode)
        return ansnode[0][1]

