class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans, temp = n, 0
        for i in range(n-k+1):
            temp = 0
            for j in range(i, i+k):
                if blocks[j] == 'W':
                    temp += 1
                # print("temp:", temp)
            ans = min(ans, temp)
        # print("ans:", ans)
        return ans