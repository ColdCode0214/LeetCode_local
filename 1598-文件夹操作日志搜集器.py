class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # ans = 0
        # n = len(logs)
        # for i in range(n):
        #     if logs[i][0] != ".": # 表示这一步的操作是移动到子文件夹中
        #         ans += 1
        #     else:
        #         if len(logs[i]) == 3:
        #             ans = max(0, ans-1)
        # return ans

        # 更快的写法
        ans = 0
        for log in logs:
            if log == "../":
                ans = max(0, ans-1)
            elif log != "./":
                ans += 1
        return ans