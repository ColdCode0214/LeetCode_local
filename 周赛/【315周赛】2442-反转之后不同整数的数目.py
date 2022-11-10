class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # nums = set(nums)
        n = len(nums)
        n2 = list()
        for i in range(n):
            temp = str(nums[i])
            temp = temp[::-1]
            cur = int(temp)
            n2.append(cur)
        nums.extend(n2)
        nums = set(nums)
        ans = len(nums)
        return ans

