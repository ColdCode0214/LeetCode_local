class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 2: return nums

        # 思路二：https://leetcode.cn/problems/single-number-iii/solution/cai-yong-fen-zhi-de-si-xiang-jiang-wen-ti-jiang-we/
        # 设置变量res，初始化为0，将res与nums中所有的数求异或，凡是出现两次的数，在异或中将抵消为0，而0异或任何数都为该数本身，故res与nums中所有数异或后的结果就是两个只出现一次的数相异或的结果
        # 样例中3->011,5->101，故异或结果为110->6符合输出
        # h的含义？？用于找到res非0的第一位？-->因为异或操作中相同为0，不同为1，因此假设答案为a,b两数，则这两者异或时第h位是不同的
        # 因此将num中的数分为两组：①第h位是0， ②第h位是1，而这两组每组包含一个答案，因此题目转换为“给定数组中只有一个数出现一次，其余数都出现两次，求只出现一次的数”
        # 此时只要将同一组中的数全部异或即可，因为相同的数会抵消为0，所以最终剩下的数即为答案

        res = 0
        for num in nums:
            res ^= num
        h = 1

        while res & h == 0:
            h <<= 1
        a, b = 0, 0
        for num in nums:
            if num & h == 0:  # 若结果为0，则说明num的第h位是0
                a ^= num
            else:  # 这组表示num第h位是1的组
                b ^= num
        return [a, b]

        # 思路一：哈希表存储每个元素出现次数
        # count = dict()
        # for a in nums:
        #     if a in count.keys():
        #         count[a] += 1
        #     else:
        #         count[a] = 1
        # ans = list()
        # for a in count.keys():
        #     if count[a] == 1:
        #         ans.append(a)
        #     if len(ans) == 2:
        #         return ans