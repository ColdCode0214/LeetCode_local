class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans, t, catch = [-1.00000 for _ in range(n)], [-1.00000 for _ in range(n)], [n for _ in range(n)]
        stack = list()
        for i in range(n):
            while stack and cars[stack[len(stack)-1]][1] > cars[i][1]:
                index = stack.pop()
                t[index] = float((cars[i][0]-cars[index][0])/(cars[index][1]-cars[i][1]))
                catch[index] = i
            stack.append(i)
        for i in range(n-1, -1, -1):
            if t[i] != -1.00000 and t[catch[i]] != -1.00000:
                while t[catch[i]] < t[i] and t[catch[i]] != -1:
                    t[i] = float((cars[ catch[catch[i]] ][0]-cars[i][0])/(cars[i][1]-cars[catch[catch[i]]][1]))
                    catch[i] = catch[catch[i]]
        return t

