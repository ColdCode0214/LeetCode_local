class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0 for _ in range(n)]
        ans = list()
        if k > 0:
            pre = sum(code[1:1 + k])
            index = k + 1
            if index == n: index = 0
        else:
            pre = sum(code[n + k:n])
            index = n + k
        for i in range(n):
            ans.append(pre)
            if k > 0 and i < n - 1:
                pre += code[index]
                index = (index + 1) % n
                pre -= code[i + 1]
            elif k < 0 and i < n - 1:
                pre += code[i]
                pre -= code[index]
                index = (index + 1) % n
        return ans




