class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        while sum(amount) > 0:
            amount.sort()
            amount.reverse()
            amount[0] -= 1
            if amount[1] > 0:
                amount[1] -= 1
            ans += 1
        return ans