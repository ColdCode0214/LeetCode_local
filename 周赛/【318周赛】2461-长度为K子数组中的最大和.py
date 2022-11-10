class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(set(nums)) < k:
            return 0
        n = len(nums)
        sum_ = [0] * (n + 1)
        for i in range(1, n + 1):
            sum_[i] = sum_[i - 1] + nums[i - 1]
        # print("sum_:", sum_)
        l, r = 0, 0
        ans = 0
        mp = dict()  # 记录元素最后出现的位置
        mp[nums[l]] = 0
        while r < n and l <= n - k:
            # print("ans:", ans)
            # print("mp:", mp)
            if r - l + 1 < k:
                # print("bk1")
                r += 1
                if r == n: break
                if nums[r] in mp:
                    # print("bk2")
                    if mp[nums[r]] == -1:
                        mp[nums[r]] = r
                    else:
                        l = mp[nums[r]] + 1
                        r = l
                        mp = dict()
                        mp[nums[l]] = l
                else:
                    # print("bk3")
                    mp[nums[r]] = r
            else:
                ans = max(ans, sum_[r + 1] - sum_[l])
                mp[nums[l]] = -1
                l += 1
                r += 1
                if r == n: break
                if nums[r] in mp:
                    if mp[nums[r]] == -1:
                        mp[nums[r]] = r
                    else:
                        l = mp[nums[r]] + 1
                        r = l
                        mp = dict()
                        mp[nums[l]] = l
                else:
                    mp[nums[r]] = r
        return ans
