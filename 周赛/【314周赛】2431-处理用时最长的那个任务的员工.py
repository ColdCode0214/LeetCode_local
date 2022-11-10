class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        lens = len(logs)
        work = 0
        temp = 0
        ans = 0
        for i in range(lens):
            # print("ans:", ans)
            if i == 0:
                work = logs[i][1]
                ans = logs[i][0]
            else:
                temp = logs[i][1] - logs[i - 1][1]
                if temp > work:
                    ans = logs[i][0]
                    work = temp
                elif temp == work:
                    if logs[i][0] < ans:
                        ans = logs[i][0]
        return ans
