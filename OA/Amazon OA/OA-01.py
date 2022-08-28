# 如果不存在返回0
from typing import List

nums = [1,2,3,4]
k= 2

def oa1t1(nums: List[int], k: int) -> int:
    n = len(nums)
    if n < k: return 0
    l, r = 0, k-1
    count = dict()
    temp= list()
    ans = 0
    while l < n-k+1 and r < n:
        temp = nums[l:r+1]
        lens = len(temp)
        if len(set(temp)) == lens:
            ans = max(ans, sum(temp))
        l += 1
        r += 1
    return ans

print(oa1t1(nums, k))

