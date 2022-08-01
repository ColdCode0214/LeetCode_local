class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        x = 1
        while x * x + x - 2 * n <= 0:
            x += 1
        if x * x + x - 2 * n == 0:
            return x
        else:
            return x - 1

