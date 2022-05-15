class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        x = 0
        y = ranges[0][0]
        for i in range(len(ranges)):
            x = max(x, ranges[i][1])
            y = min(y, ranges[i][0])
        if right > x or left < y:
            return False
        a = [0 for i in range(x+1)]
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                a[j] = 1
        for i in range(left,right+1):
            if a[i] != 1:
                return False
        return True