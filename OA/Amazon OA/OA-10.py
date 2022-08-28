'''
Amazon OA10(Leetcode 2104)
You are given an integer array nums.
The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
Return the sum of all subarray ranges of nums
A subarray is a contiguous non-empty sequence of elements within an array.
'''
from typing import List

nums = [1,2,3]

def oa1t10(nums: List[int]) -> int:
    n = len(nums)
    # 令第i个元素成为最大值的次数为maxi次，成为最小值的次数为mini次
    # 则nums中每个元素的贡献值是：nums[i]*(maxi-mini)
    # 最终答案是所有贡献值之和
    # 如何找到一个数成为最大值/最小值的次数
    stack = list()
    for i in range(n):
        while stack and nums[stack[len(stack)]] > nums[i]:


