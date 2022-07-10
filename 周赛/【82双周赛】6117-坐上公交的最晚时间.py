class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        n, m = len(buses), len(passengers)
        i, j, count = 0, 0, 0
        t = 0
        while i < n and j < m:
            print("i:", i, " j:", j)
            if i == n - 1:  # 最后一辆
                if count == capacity - 1:  # 仅剩一个空位
                    t = min(buses[i], passengers[j] - 1)
                    break
                else:  # 多个空位
                    if passengers[j] > buses[i]:  # 后面的人不会再上来了
                        t = buses[i]
                        break
                    else:
                        if j == m - 1:  # 最后一个人
                            t = buses[i]
                            break
                        else:  # 还有多个人
                            j += 1
                            count += 1
            else:  # 不是最后一辆
                if count < capacity:  # 有空位
                    if passengers[j] <= buses[i]:  # 时间上满足上车条件
                        if j == m - 1:  # 最后一个人
                            t = buses[n - 1]
                            break
                        else:
                            j += 1
                            count += 1

                    else:  # 时间上不满足上车条件
                        i += 1
                        count = 0

                else:  # 满员
                    count = 0
                    i += 1

        print("t:", t)
        while t in passengers:
            t -= 1
        return t
