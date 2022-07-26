class MyCalendarTwo:
    # 本题初始想到的思路是使用哈希存储每个时间点的预订次数，当次数超过时直接返回，若未返回则属于成功预订
    # 但此方法有超时的风险；并且没有合理的使用“时间是连续的”这一条件
    # 经查看题解学习“插旗法”
    def __init__(self):
        self.time = dict()

    def book(self, start: int, end: int) -> bool:
        # 首先将最新的日程更新到日历中
        # 与之前思路的区别是：插旗法只更新起点&终点，中间的部分不作处理
        if start in self.time.keys():
            self.time[start] += 1
        else:
            self.time[start] = 1
        if end in self.time.keys():
            self.time[end] -= 1
        else:
            self.time[end] = -1

        # 注意，需要保证time是按键的升序排列的
        def sortDict(data) -> dict:
            return dict(sorted(data.items(), key=operator.itemgetter(0), reverse=False))

        self.time = sortDict(self.time)

        # 定义一个“游标”，用于“遍历”当前的日历
        cur = 0

        # 若某时间段预订超过限制，则该时间段的起始时间点也一定是超过限制的，因此并不需要遍历所有的时间，而仅需遍历头尾时间点
        # 遍历头时间点用于判断以当前时段为头的日程是否违反预定规则
        # 遍历尾时间点则用于标记退出当前时段
        # 因此插旗法很好的利用了时间连续这一条件

        for a in self.time.keys():
            cur += self.time[a]
            if cur > 2:  # 如果出现三重预订，也一定是本次新增的日程导致的，因此直接回退本次的新增日程
                self.time[start] -= 1
                self.time[end] += 1
                return False
        return True

        # 如果一个时间点既是某日程的起始时间，又是另一日程的结束时间，+1后又-1是否会导致错误？？

        # for i in range(start, end):
        #     if i in self.time.keys() and self.time[i] == 2: return False
        # for i in range(start, end):
        #     if i in self.time.keys():
        #         self.time[i] += 1
        #     else:
        #         self.time[i] = 1
        # return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)