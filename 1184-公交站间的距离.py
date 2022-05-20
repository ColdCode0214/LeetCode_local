class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        ans1, ans2 = 0, 0
        all = sum(distance)
        for i in range(min(start, destination), max(start, destination)):
            ans1 += distance[i]
        ans2 = all - ans1
        return min(ans1, ans2)