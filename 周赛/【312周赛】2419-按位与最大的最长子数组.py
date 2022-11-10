class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ = max(nums)
        n = len(nums)
        ans = 0
        i = 0
        while i < n:
            if nums[i] == max_:
                index = i + 1
                for j in range(i + 1, n):
                    if nums[j] != max_:
                        index = j
                        break
                    if j == n - 1:
                        index = j + 1
                ans = max(ans, index - i)
                i = index + 1
            else:
                i += 1
        # for i in range(n):
        #     if nums[i] == max_:
        #         index = i+1
        #         for j in range(i+1, n):
        #             if nums[j] != max_:
        #                 index = j
        #                 break
        #             if j == n-1:
        #                 index = j+1
        #         ans = max(ans, index-i)
        #         i = index+1
        #     print("i:", i)
        return ans
