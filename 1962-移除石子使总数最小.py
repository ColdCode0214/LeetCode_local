class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        neg = list()
        heapq.heapify(neg)
        for a in piles:
            heapq.heappush(neg, -a)
        for i in range(k):
            temp = heapq.heappop(neg)
            temp = floor(temp/2)
            heapq.heappush(neg, temp)
        return -sum(neg)
