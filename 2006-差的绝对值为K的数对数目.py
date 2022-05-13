class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        fre = Counter()
        ans = 0
        for a in nums:
            ans += fre[a+k] + fre[a-k]
            fre[a] += 1 #一边求解（累加）需要返回的ans的数值、一边统计每个元素出现的次数
        return ans
