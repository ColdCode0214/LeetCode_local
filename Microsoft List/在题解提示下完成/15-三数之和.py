class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = list()
        if n < 3:
            return ans
        nums.sort()
        for k in range(n):
            if k == 0 or nums[k] != nums[k-1]:
                if nums[k] > 0:
                    break
                else:
                    i, j = k+1, n-1
                    while i < j:
                        if nums[k]+nums[i]+nums[j] < 0:
                            i += 1
                        elif nums[k]+nums[i]+nums[j] > 0:
                            j -= 1
                        else:
                            if (i == k+1 and j == n-1) or nums[i] != nums[i-1] or nums[j] != nums[j+1]:
                                ans.append([nums[k], nums[i], nums[j]])
                            i += 1
                            j -= 1

        return ans