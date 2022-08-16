class OrderedStream:

    # def __init__(self, n: int):
    #     self.ptr = 1
    #     self.queue = ["" for _ in range(n)]
    #     self.n = n


    # def insert(self, idKey: int, value: str) -> List[str]:
    #     self.queue[idKey-1] = value
    #     # print("queue:", self.queue)
    #     cp = self.ptr - 1
    #     ans = list()
    #     while cp < self.n and len(self.queue[cp]) > 0:
    #         ans.append(self.queue[cp])
    #         cp += 1
    #     # print("cp:", cp)
    #     if len(ans) != 0: self.ptr = cp + 1
    #     # print("ans:", ans)
    #     return ans

    def __init__(self, n: int):
        self.queue = [""] * (n+1)
        self.ptr = 1
        self.n = n


    def insert(self, idKey: int, value: str) -> List[str]:
        ans = list()
        self.queue[idKey] = value
        while self.ptr <= self.n and len(self.queue[self.ptr]) != 0:
            ans.append(self.queue[self.ptr])
            self.ptr += 1

        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)