class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        # 找numsDivide中所有元素的最大公约数？？不一定要最大，如果nums中最小值是1那所有都OK
        count = len(nums)
        mp = dict()
        for a in nums:
            if a in mp.keys():
                mp[a] += 1
            else:
                mp[a] = 1
        nums = list(set(nums))
        heapq.heapify(nums)

        ans = 0
        numsDivide = list(set(numsDivide))
        n, m = len(nums), len(numsDivide)
        print("numsDivide:", numsDivide)
        print("nums:", nums)
        while nums:
            x = heappop(nums)
            print("x:", x)
            flag = 0
            for a in numsDivide:
                if a % x != 0:
                    ans += mp[x]
                    flag = 1
                    break
            if flag == 0:
                return ans
        if ans == count:
            return -1
        else:
            return ans

