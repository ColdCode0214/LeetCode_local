class Solution:
    def maximumSwap(self, num: int) -> int:
        arr, arr2 = list(), list()
        cp = num
        while num > 0:
            arr.append(num % 10)
            arr2.append(num % 10)
            num = int(num / 10)
        arr.reverse()  # 原数原序列
        arr2.sort()
        arr2.reverse()  # 降序排列
        index = -1
        n = len(arr)
        for i in range(n):
            if arr[i] != arr2[i]:
                index = i
                break

        if index == -1:
            return cp
        else:
            for i in range(n - 1, -1, -1):
                if arr[i] == arr2[index]:
                    arr[index], arr[i] = arr[i], arr[index]
                    break
            ans = 0
            for i in range(n):
                ans *= 10
                ans += arr[i]
            return ans