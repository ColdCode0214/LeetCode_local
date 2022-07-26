class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter(nums)
        # print(count)
        nums = set(nums)
        mp = dict()
        c = list()
        for a in nums:
            # a2 = bin(a)
            count = 0
            while a > 0:
                if a % 2 == 1:
                    count += 1
                    a -= 1
                a = int(a / 2)
            c.append(count)
        mp2 = dict()
        lens = len(c)
        # print("c:", c)
        ans = 0
        for a in c:
            # if a >= int(k/2):
            #     if a in mp2.keys():
            #         mp2[a] += 1
            #     else:
            #         mp2[a] = 1
            if a in mp2.keys():
                mp2[a] += 1
            else:
                mp2[a] = 1
        # print("mp2:", mp2)
        for a in mp2.keys():
            # if mp2[a] >= k-1:
            #     ans += lens
            #     print("ans1:", ans)
            #     print("a:", a)
            # else:
            # for b in mp2.keys():
            #     if a+b >= k:
            #         ans += mp2[a]*mp2[b]
            for b in mp2.keys():
                if a + b >= k:
                    ans += mp2[a] * mp2[b]
                # print("ans2:", ans)
        return ans

#         c.sort()
#         ans = 0
#         c.reverse()
#         lens = len(c)
#         for i in range(lens):
#             if c[i] >= k-1: ans += (lens-i-1)*2+1
#             else:

#                 if c[i] < int(k/2): return ans
#                 for j in range(i,lens):
#                     if c[i]+c[j] >= k:
#                         if i == j:
#                             ans += 1
#                         else: ans += 2
#                     else: break
#         return ans

