class LUPrefix:

    def __init__(self, n: int):
        self.vl = [0]*(n+1)
        self.index = 0
        self.n = n


    def upload(self, video: int) -> None:
        self.vl[video] = 1
        while self.index < self.n and self.vl[self.index+1] == 1:
            self.index += 1

    def longest(self) -> int:
        return self.index



# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()