class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2
        diff = list()
        for i in range(n):
            diff.append(abs(nums1[i] - nums2[i]))

        diff.sort()
        diff.reverse()
        diff.append(0)
        print(diff)
        for i in range(n):
            x = int(k / (i + 1))  # 计算当前剩余的K次操作数可以满足当前子序列可以操作的轮数
            print("x:", x)
            need = diff[i] - diff[i + 1]  # 当前子序列想达到其后元素的值所需要的操作次数
            print("need:", need)
            if x < need:  # 当前操作数不足
                for j in range(i + 1):
                    diff[j] = diff[i] - x
                rest = k - x * (i + 1)
                for j in range(rest):
                    diff[j] -= 1

                ans = 0
                for j in range(n):
                    ans += diff[j] * diff[j]
                return ans

            else:  # 当前操作数有剩余
                k -= (diff[i] - diff[i + 1]) * (i + 1)
                # print("k:", k)
                # for j in range(i):
                #     diff[j] = diff[i+1]
        return 0


