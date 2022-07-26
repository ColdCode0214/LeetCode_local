class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 思路三：使用集合限制所有元素的出现次数均为1，再求其三倍，减去原数组总和，得到的差是待求答案的两倍
        return (sum(set(nums))*3-sum(nums))//2

        # 思路一：排序后查找与前后元素不等的元素(45.97%+38.66%)
        # nums.sort()
        # n = len(nums)
        # if n == 1: return nums[0]
        # if nums[0] != nums[1]: return nums[0]
        # if nums[n-1] != nums[n-2]: return nums[n-1]
        # for i in range(1, n-1):
        #     if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
        #         return nums[i]

        # 思路二：使用哈希表存储每个元素出现的次数(89.34%+41.26%)
        # count = dict()
        # for a in nums:
        #     if a in count.keys():
        #         count[a] += 1
        #     else:
        #         count[a] = 1
        # for a in count.keys():
        #     if count[a] == 1:
        #         return a