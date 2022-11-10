class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if sum(nums) < target:
            return 0
        total = 0
        start, end = 0, 0
        ans = n
        while end < n:
            total += nums[end]
            while total >= target:
                ans = min(ans, end-start+1)
                total -= nums[start]
                start += 1
            end += 1
        return ans
        
        # n = len(nums)
        # if sum(nums) < target:
        #     return 0
        # l, r = 0, 1
        # ans = n
        # sum_ = [0]*(n+1)
        # for i in range(1, n+1):
        #     sum_[i] = sum_[i-1] + nums[i-1]
        # while l < n:
        #     if sum_[r] - sum_[l] < target and r < n:
        #         r += 1
        #     elif sum_[r] - sum_[l] >= target:
        #         ans = min(ans, r-l)
        #         l += 1
        #     else:
        #         break
        # return ans