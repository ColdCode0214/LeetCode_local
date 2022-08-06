class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        ans = 0
        n = len(tasks)
        day = dict()
        count = 1
        for i in range(n):
            # print(day)
            if tasks[i] not in day:
                day[tasks[i]] = count
                count += 1
            else:
                if count-day[tasks[i]] <= space:
                    count = day[tasks[i]] + space +1
                day[tasks[i]] = count
                count += 1
        count -= 1
        return count