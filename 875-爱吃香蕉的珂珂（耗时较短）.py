class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n, max_p = len(piles), max(piles)
        if n == h: return max_p
        sum_p = sum(piles)

        left_k, right_k = (sum_p - 1) // h + 1, min(max_p, (sum_p - n) // (h - n + 1) + 1)

        while left_k < right_k:
            mid_k = (left_k + right_k) // 2

            time = 0
            for p in piles:
                time += (p - 1) // mid_k + 1
                if time > h: break

            if time > h:
                left_k = mid_k + 1
            else:
                right_k = mid_k
        return left_k