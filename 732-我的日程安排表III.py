class MyCalendarThree:
    # 首先再次尝试“插旗法”
    def __init__(self):
        self.time = dict()

    def book(self, start: int, end: int) -> int:
        if start in self.time.keys(): self.time[start] += 1
        else: self.time[start] = 1
        if end in self.time.keys(): self.time[end] -= 1
        else: self.time[end] = -1

        def sortDict(data) -> dict:
            return dict(sorted(data.items(), key=operator.itemgetter(0), reverse=False))

        self.time = sortDict(self.time)

        cur, ans = 0, 0

        for a in self.time.keys():
            cur += self.time[a]
            ans = max(ans, cur)
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)