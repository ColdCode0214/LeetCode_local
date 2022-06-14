class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = nums[0]+nums[1]+nums[2]
        for k in range(n-2):
            i, j = k+1, n-1
            while i < j:
                if nums[k] + nums[i] + nums[j] == target:
                    return target
                elif nums[k] + nums[i] + nums[j] > target:
                    if abs(nums[k] + nums[i] + nums[j]-target) < abs(ans-target):
                        ans = nums[k] + nums[i] + nums[j]
                    #print("ans1:",ans)
                    j -= 1
                else:
                    if abs(nums[k] + nums[i] + nums[j]-target) < abs(ans-target):
                        ans = nums[k] + nums[i] + nums[j]
                    #print("ans2:",ans)
                    i += 1
        return ans

