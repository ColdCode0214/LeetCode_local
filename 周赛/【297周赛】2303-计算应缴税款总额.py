class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        brackets.insert(0, [0, 0])
        n = len(brackets)
        ans = 0

        # while income > 0:
        for i in range(1, n, 1):
            amount = min(income, brackets[i][0] - brackets[i - 1][0])
            ans += amount * brackets[i][1] / 100
            income -= amount
            if income <= 0:
                break
        return ans