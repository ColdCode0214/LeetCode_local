class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        lens = len(queries)
        ans = list()
        nums.sort()
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
        for i in range(lens):
            for j in range(n):
                if pre[j + 1] > queries[i]:
                    ans.append(j)
                    break
                if j == n - 1:
                    ans.append(n)
        return ans
        # for i in range(lens): # 循环query
        #     dp = [0]*n
        #     count = [0]*n
        #     for j in range(n): # 循环数组nums
        #         if nums[0] < queries[i]:
        #             dp[0] = 1
        #             count[0] = nums[0]
        #         for k in range(j):
        #             if count[k]+nums[j] <= queries[i] and dp[k]+1 > dp[j]:
        #                 count[j] = count[k] + nums[j]
        #                 dp[j] = dp[k]+1
        #     # print("dp:", dp)
        #     ans.append(max(dp))
        # return ans



