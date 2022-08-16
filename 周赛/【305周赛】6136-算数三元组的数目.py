class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1, n):
                    if nums[j]-nums[i]==nums[k]-nums[j]==diff:
                        # print(nums[j], nums[i], nums[k])
                        ans += 1
                        # break
        return ans