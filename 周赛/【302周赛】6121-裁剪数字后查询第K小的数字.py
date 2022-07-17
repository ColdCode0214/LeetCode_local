class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n, m, k = len(nums), len(queries), len(nums[0])  # k表示统一的字符长度
        mp = dict()  # 存储已有分割
        ans = list()
        temp = list()
        for i in range(m):  # 外层循环query
            if queries[i][1] in mp.keys():  # 当前分割曾经有过
                temp = mp[queries[i][1]]
            else:
                temp = list()  # 每次查询对应的分割
                for j in range(n):  # 内层循环num
                    temp.append(int(nums[j][k - queries[i][1]:k]))
                mp[queries[i][1]] = temp
            # for i in range(m):
            arr = mp[queries[i][1]]
            arr2 = list()
            for a in arr:
                arr2.append(a)
            arr2.sort()
            res = arr2[queries[i][0] - 1]
            index = 0
            for j in range(n):
                if arr2[j] == res:
                    index = j  # 记录排好序的数组中第一次出现答案数字时的下标
                    break
            if index == queries[i][0] - 1:  # 如果答案数第一次出现的位置和想找的第x小的位置一致，则说明答案坐标就是arr数组中第一次出现res的位置
                for j in range(n):
                    if arr[j] == res:
                        ans.append(j)
                        break
            else:
                cur, target = 0, queries[i][0] - index
                for j in range(n):
                    if arr[j] == res:
                        cur += 1
                    if cur == target:
                        ans.append(j)
                        break
        return ans





