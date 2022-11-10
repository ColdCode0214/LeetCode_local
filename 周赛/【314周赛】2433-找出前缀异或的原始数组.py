class Solution:

    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        ans = []
        ans.append(pref[0])
        for i in range(1, n):
            ans.append(pref[i] ^ pref[i - 1])
        return ans
        # n = len(pref)
        # ans = []
        # ans.append(pref[0])
        # bin_ = []
        # for i in range(n):
        #     bin_.append(str(bin(pref[i]))[2:])
        # # print("bin_:", bin_)
        # for i in range(1, n):
        #     cur = bin_[i]
        #     pre = bin_[i-1]
        #     # print("cur:", cur, " pre:", pre)
        #     lencur, lenpre = len(cur), len(pre)
        #     if lencur > lenpre:
        #         pre = '0'*(lencur-lenpre)+pre
        #     elif lenpre > lencur:
        #         cur = '0'*(lenpre-lencur)+cur
        #     res = ''
        #     for j in range(len(cur)):
        #         # print("res1:", res)
        #         if cur[j] == '0': # 相同
        #             res += pre[j]
        #         else: # 不同
        #             if pre[j] == '0':
        #                 res += '1'
        #             else:
        #                 res += '0'
        #     temp = 0
        #     print("res:", res)
        #     for k in range(len(res)):
        #         print("k:", k)
        #         temp = temp*2+int(res[i])
        #     ans.append(temp)
        # return ans

