class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # n = len(arr)
        # ans = 0
        # length = 1
        # if n%2 == 1:
        #     limit = n
        # else:
        #     limit = n-1
        # while length <= limit:
        #     for i in range(0, n+1-length):
        #         ans += sum(arr[i: i+length])
        #     length += 2
        # return ans

        # 方法二：前缀和
        sumnum = list()
        sumnum.append(0)
        n = len(arr)
        index = 0
        for i in range(n):
            sumnum.append(sumnum[index]+arr[i])
            index += 1
        if n%2 == 1: limit = n
        else: limit = n-1
        length = 1
        ans = 0
        while length <= limit:
            for i in range(0, n+1-length):
                ans += sumnum[i+length] - sumnum[i]
            length += 2
        return ans