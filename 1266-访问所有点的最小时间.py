class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1: return 0
        ans = 0
        for i in range(1, n):
            x1, x2 = points[i][0], points[i-1][0]
            y1, y2 = points[i][1], points[i-1][1]
            x = abs(x1-x2)
            y = abs(y1-y2)
            # x = abs(points[i][0]-points[i-1][0])
            # y = abs(points[i][1]-points[i-1][1])
            ans += min(x, y)
            ans += abs(x-y)
        return ans