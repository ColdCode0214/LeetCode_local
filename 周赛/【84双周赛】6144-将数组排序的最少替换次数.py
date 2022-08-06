class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        '''
        1、一个数越大，留给前面的数的空间越多
        2、使用贪心算法，最后一个数不需要拆分，并且它的值将决定其前面的值的上限，从倒数第二个数开始考虑
        3、假设当前数值为x，其后方的数为y
            1）若x<=y，则无需操作
            2）若x>y，则需要拆分x，x拆分后的值不能超过y，但其最小值还要尽量大
        '''

        ans = 0
        n = len(nums)
        last = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i] <= last:
                last = nums[i]
            else:
                k = int(ceil(nums[i]/last))
                ans += k-1
                last = int(floor(nums[i]/k))
        return ans