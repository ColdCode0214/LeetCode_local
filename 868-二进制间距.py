class Solution:
    def binaryGap(self, n: int) -> int:
        nums = list()
        while n > 0:
            nums.append(n%2)
            n = int(n/2)
        lens = len(nums)
        ans = 0
        pre = -1
        for i in range(lens):
            if nums[i] == 1:
                if pre != -1:
                    ans = max(ans, i-pre)
                pre = i
        return ans