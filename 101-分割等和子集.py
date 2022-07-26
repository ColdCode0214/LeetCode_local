class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 如果能够分成相等的两部分，则每一部分的和为整个数组总和的一半
        # 因此，如果总和是奇数，则一定是FALSE
        sum_num = sum(nums)
        if sum_num % 2 == 1: return False
        target = int(sum_num / 2)
        print("target:", target)
        # 使用动态规划求解
        # dp[i]表示从值i能否由数组中的元素组成,dp数组的长度设置为target+1,多一位可以让下标和target的值直接对应
        dp = [False for _ in range(target + 1)]
        # nums.sort()
        for i in range(len(nums)):
            # 接下来根据当前遍历到的数组元素的大小判断dp中都有哪些值可以被组成
            # 其中只需要判断大于等于当前元素的数值（能否被组成）， 因为比nums[i]小的值一定不能由nums[i]组成；比nums[i]大的值则有可能由nums[i]和其他元素共同组成
            for j in range(target, -1, -1):
                if j < nums[i]:
                    break
                elif j == nums[i]:
                    dp[j] = True
                else:
                    dp[j] = dp[j - nums[i]] or dp[j]
                if dp[target] == True: return True
        return False


