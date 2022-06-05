class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        a = max(candies)
        for i in candies:
            if i+extraCandies >= a:
                ans.append(True)
            else:
                ans.append(False)
        return ans