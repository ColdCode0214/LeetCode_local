class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        temp = 0
        for i in gain:
            temp += i
            ans = max(temp, ans)
        return ans