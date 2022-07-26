class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        q = list()
        for i in range(n):
            if nums[i] == 0:
                q.append(i)
        lens = len(q)
        for i in range(lens):
            if i == 0:
                count = 1
            else:
                if q[i] == q[i - 1] + 1:
                    count += 1
                else:
                    ans += int(((count + 1) * count) / 2)
                    count = 1
            if i == lens - 1:
                ans += int(((count + 1) * count) / 2)
        return ans
