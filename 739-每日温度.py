class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 新建单调栈用于存储访问了、但还没找到下一最高温度的下标
        stack = list()
        # 初始化ans均为0，这样最终升剩在栈中找不到更高温度的就默认为0
        n = len(temperatures)
        ans = [0 for _ in range(n)]
        for i in range(n):
            while stack and temperatures[stack[len(stack)-1]] < temperatures[i]:
                index = stack.pop()
                ans[index] = i-index
            stack.append(i)
        return ans