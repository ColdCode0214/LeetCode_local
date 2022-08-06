class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.cq = deque()
        self.cur = 0

    def enQueue(self, value: int) -> bool:
        if self.cur < self.k:
            self.cq.append(value)
            self.cur += 1
            return True
        else: return False

    def deQueue(self) -> bool:
        if self.cur == 0: return False
        else:
            self.cq.popleft()
            self.cur -= 1
            return True

    def Front(self) -> int:
        if self.cur == 0: return -1
        else:
            return self.cq[0]

    def Rear(self) -> int:
        if self.cur == 0: return -1
        else:
            return self.cq[self.cur-1]

    def isEmpty(self) -> bool:
        if self.cur == 0:
            return True
        else:
            return False


    def isFull(self) -> bool:
        if self.cur == self.k:
            return True
        else: return False



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()