class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        if n == 1: return True
        vis = [False] * n

        q = list()  # 存储可以进入的房间的下标
        q.append(0)
        while q:
            if vis[q[0]] == False:
                q.extend(rooms[q[0]])
                vis[q[0]] = True
            q.pop(0)
        # for a in vis:
        #     if a == False: return False
        return all(vis)

