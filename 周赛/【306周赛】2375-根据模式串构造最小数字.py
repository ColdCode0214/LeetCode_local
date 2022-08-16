class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        if pattern[n - 1] == 'I':
            pattern += "I"
        else:
            pattern += 'D'
        ans = [0 for _ in range(n + 1)]

        count = 1
        stack = list()  # 用栈记录访问过的pattern的下标，如果是D就存起来，如果遇到I就把之前的pop出来
        for i in range(n + 1):
            if pattern[i] == 'I':
                ans[i] = count
                count += 1
                while stack:
                    temp = stack.pop()
                    ans[temp] = count
                    count += 1
            else:
                stack.append(i)
        while stack:
            temp = stack.pop()
            ans[temp] = count
            count += 1
        res = "".join(str(i) for i in ans)
        # print("res:", res)
        return res

