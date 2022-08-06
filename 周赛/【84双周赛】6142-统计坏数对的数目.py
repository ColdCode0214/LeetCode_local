class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        '''
        本题的关键是两个转化：
        1. 求坏数对数目转化为求“数对总数-好数对数”
        2. 好数对的标准中j - i == nums[j] - nums[i]应通过移项变为j-nums[j]==i-nums[i]=diff，这样利用diff一定这一特征可以使用map存储满足差值为diff的元素的数量
        '''
        n = len(nums)
        numpair = int(n * (n - 1) / 2)
        diff = dict()
        for i in range(n):
            if i - nums[i] in diff:
                numpair -= diff[i - nums[i]]
                diff[i - nums[i]] += 1
            else:
                diff[i - nums[i]] = 1
        return numpair

        '''
        1.上面的方法是利用数对有序性（要求i<j）的特点在求数组下标与元素的差的同时就把该元素所构成的好数对的数目从总数对数目中减去
        2.下面的方法是统计出每个差所包含的元素总数后统一求和;只出现过一次的差也不会影响结果，因为在计算过程中会因为n-1=0使结果为0，因此不会影响到总结果    
        '''
        # good = 0
        # for a in diff:
        #     good += int(diff[a]*(diff[a]-1)/2)
        # return numpair-good
