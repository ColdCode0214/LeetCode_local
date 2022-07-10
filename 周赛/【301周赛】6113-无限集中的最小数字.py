class SmallestInfiniteSet:

    def __init__(self):
        self.l = list()
        for i in range(1000):
            self.l.append(i + 1)

    def popSmallest(self) -> int:
        temp = self.l[0]
        self.l.pop(0)
        return temp

    def addBack(self, num: int) -> None:
        if num not in self.l:
            self.l.append(num)
            self.l.sort()

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)