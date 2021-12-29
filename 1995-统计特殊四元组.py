class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        #nums.sort()
        n = len(nums)
        ans = 0
        for a in range(n-3):
            for b in range(a+1, n-2):
                for c in range(b+1, n-1):
                    for d in range(c+1, n):
                        if(nums[a] + nums[b] + nums[c] == nums[d]):
                            ans += 1
        return ans