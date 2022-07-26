class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 以下为参考用时击败100%用户的代码
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans

        # 以下为参考题解完成的代码，用时击败6.41%
        # n = len(temperatures)
        # ans = [0 for _ in range(n)]
        # stack = list()
        # for i in range(n):
        #     if len(stack) == 0: stack.append(i)
        #     else:
        #         while len(stack) > 0 and temperatures[i] > temperatures[stack[len(stack)-1]]:
        #             ans[stack[len(stack)-1]] = i-stack[len(stack)-1]
        #             stack.pop()
        #         stack.append(i)
        # return ans

        # 以下是此题的初始思路，此方法会超时
        # n = len(temperatures)
        # if n == 1: return [0]
        # l, r = 0, 1
        # # 基础思路：固定l指针作为当前循环的下标，r为搜索下一更高气温的下标，如果能搜到则加入答案列表，如果r=n时还没搜到则说明搜不到，答案中加入0
        # # 优化：假设r为对应t[l]的答案，如果t[l+1]=t[l],则t[l+1]对应的答案也是r；如果t[l+1]>t[l]，则t[l+1]对应答案的下标一定大于r；如果t[l+1]<t[l]则与r的关系不一定
        # # 优化：如果t[l]是数组从当前位置到末尾的最大值，那么ans一定是0；并且只有这种情况会是0
        # ans = list()
        # for l in range(n):
        #     if temperatures[l] == max(temperatures[l:n]): # 为的情况
        #         ans.append(0)
        #     else: # 一定存在的情况
        #         if l == 0: r = 1
        #         else:
        #             if temperatures[l] == temperatures[l-1]:
        #                 ans.append(ans[len(ans)-1]-1)
        #                 r = n
        #             else: # 包含当前温度高于前一天、当前温度低于前一天
        #                 if temperatures[l] > temperatures[l-1]: r = pre
        #                 else: r = l+1
        #         while r < n:
        #             if temperatures[r] > temperatures[l]:
        #                 ans.append(r-l)
        #                 pre = r
        #                 break
        #             r += 1
        # return ans
