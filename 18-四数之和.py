#本题和三数之和的的区别（同时也是一处易错点）是不能通过前一/两个数之和大于target就break
#因为有可能当前数之和大于target，但后面还可能是负数，导致和再次降下来（例：[1,-2,-5,-4,-3,3,3,5], -11）
#而三数之和之所以可以提前break是因为那道题的target相当于0，而凡是最外层循环的数已经大于了0，后面的值一定都是正数的，和不可能再下降
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = list()
        for p in range(n-3):
            if p == 0 or nums[p] != nums[p-1]:
                for q in range(p+1, n-2):
                    if q == p+1 or nums[q] != nums[q-1]:
                        i, j = q+1, n-1
                        while i < j:
                            if nums[p]+nums[q]+nums[i]+nums[j] > target:
                                j -= 1
                            elif nums[p]+nums[q]+nums[i]+nums[j] < target:
                                i += 1
                            else:
                                #print(nums[p], " ", nums[q], " ", nums[i], " ", nums[j])
                                if (i == q+1 and j == n-1) or nums[i] != nums[i-1] or nums[j] != nums[j+1]:
                                    ans.append([nums[p], nums[q], nums[i], nums[j]])
                                i += 1
                                j -= 1
        return ans
