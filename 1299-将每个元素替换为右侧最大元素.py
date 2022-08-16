class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # n = len(arr)
        # ans = list()
        # rec = arr[n-1]
        # for i in range(n-1, -1, -1):
        #     if i == n-1:
        #         ans.append(-1)
        #     else:
        #         rec = max(rec, arr[i+1])
        #         ans.insert(0, rec)
        # return ans

        # 方法二： 原地修改
        n = len(arr)
        max_ = -1
        for i in range(n - 1, -1, -1):
            arr[i], max_ = max_, max(max_, arr[i])
        return arr

