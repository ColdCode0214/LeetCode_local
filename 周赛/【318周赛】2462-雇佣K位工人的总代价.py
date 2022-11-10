class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans, n = 0, len(costs)
        if candidates * 2 < n:
            pre = costs[:candidates]
            heapq.heapify(pre)
            suf = costs[-candidates:]
            heapq.heapify(suf)
            i, j = candidates, n-1-candidates
            while k and i <= j:
                if pre[0] <= suf[0]:
                    ans += heapreplace(pre, costs[i])
                    i += 1
                else:
                    ans += heapreplace(suf, costs[j])
                    j -= 1
                k -= 1
            costs = pre + suf
        costs.sort()
        return ans + sum(costs[:k])