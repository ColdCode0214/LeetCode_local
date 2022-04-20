class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0:
                        ans+=1
                    else:
                        if grid[i-1][j] == 0:
                            ans+=1
                    if j == 0:
                        ans+=1
                    else:
                        if grid[i][j-1] == 0:
                            ans+=1
        return ans*2

# 题解思路(from Perpetual Resonance)：一束光从 x 轴正负两个方向分别照到岛上时照到的边的数量是相等的，从 y 轴正负两个方向分别照到岛上时照到的边的数量也是相等的
# 所以每个坐标轴只需计算一个方向，最后把答案乘二即可
# 经评论提醒，之前没有表达清除，这束光可以想象成从斜上方照向岛屿，因为要保证某一方向上所有的边都被照到
# 每个格子如果左边是水说明照的到，否则照不到，上方同理
