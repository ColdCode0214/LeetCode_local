class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = list()
        n = len(prices)
        ans = list()
        for i in range(n):
            while stack and prices[stack[len(stack) - 1]] >= prices[i]:
                temp = stack.pop()
                prices[temp] -= prices[i]
            stack.append(i)

        return prices

