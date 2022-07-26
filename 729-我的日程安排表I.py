class MyCalendar:
    # 插旗法
    def __init__(self):
        self.time = dict()

    # def sortDict(self, data: dict) -> dict:
    #     return dict(sorted(data.items(), key=operator.itemgetter(0), reverse=False))

    def book(self, start: int, end: int) -> bool:
        if start in self.time.keys():
            self.time[start] += 1
        else:
            self.time[start] = 1
        if end in self.time.keys():
            self.time[end] -= 1
        else:
            self.time[end] = -1

        def sortDict(data) -> dict:
            return dict(sorted(data.items(), key=operator.itemgetter(0), reverse=False))

        self.time = sortDict(self.time)

        cur = 0

        for a in self.time.keys():
            cur += self.time[a]
            if cur > 1:
                self.time[start] -= 1
                self.time[end] += 1
                return False
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)