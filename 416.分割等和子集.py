class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        target = int(sum(nums)/2)
        lens = len(nums)
        #dp = [[False]*(target+1)]*lens #这样初始化会导致修改二维数组中一个数时直接改掉了一列，原因参考https://blog.csdn.net/qq_36561737/article/details/114842228
        dp = [[False for _ in range(target+1)] for _ in range(lens)]
        
        for i in range(lens):
            for j in range(target+1):
                if i == 0:
                    if j == nums[i]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                elif j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                elif j == nums[i]:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                if j == target and dp[i][j] == True:
                    return True
        return False
