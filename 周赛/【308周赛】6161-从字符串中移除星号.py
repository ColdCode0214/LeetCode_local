class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        stack = list()
        for i in range(n):
            if s[i] == "*":
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)