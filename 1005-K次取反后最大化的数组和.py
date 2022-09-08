class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k > 0:
            temp = heapq.heappop(nums)
            temp = -temp
            heapq.heappush(nums, temp)
            k -= 1
        return sum(nums)