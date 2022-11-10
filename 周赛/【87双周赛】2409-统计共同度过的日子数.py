class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        ma1, da1, ma2, da2, mb1, db1, mb2, db2 = int(arriveAlice[0:2]), int(arriveAlice[3:5]), int(
            leaveAlice[0:2]), int(leaveAlice[3:5]), int(arriveBob[0:2]), int(arriveBob[3:5]), int(leaveBob[0:2]), int(
            leaveBob[3:5])
        md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # print(ma1, da1, ma2, da2, mb1, db1, mb2, db2)
        # m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12 = 31*[0], 28*[0], 31*[0], 30*[0], 31*[0], 30*[0], 31*[0], 31*[0], 30*[0], 31*[0], 30*[0], 31*[0]
        m = [1 * [0], 32 * [0], 29 * [0], 32 * [0], 31 * [0], 32 * [0], 31 * [0], 32 * [0], 32 * [0], 31 * [0],
             32 * [0], 31 * [0], 32 * [0]]

        for i in range(ma1, ma2 + 1):
            if i == ma1:
                for j in range(da1, len(m[i])):
                    m[i][j] += 1
            else:
                for j in range(len(m[i])):
                    m[i][j] += 1
            if i == ma2:
                for j in range(da2 + 1, len(m[i])):
                    m[i][j] -= 1

        for i in range(mb1, mb2 + 1):
            if i == mb1:
                for j in range(db1, len(m[i])):
                    m[i][j] += 1
            else:
                for j in range(len(m[i])):
                    m[i][j] += 1
            if i == mb2:
                for j in range(db2 + 1, len(m[i])):
                    m[i][j] -= 1

        # for x in range(ma1, ma2+1):
        #     if x == ma1:
        #         for j in range(da1, len(m[x])):
        #             m[x][j] += 1
        #     elif x == ma2 and ma1 != ma2:
        #         for j in range(da2+1):
        #             m[x][j] += 1
        #     else:
        #         for j in range(len(m[x])):
        #             m[x][j] += 1
        # for x in range(mb1, mb2+1):
        #     if x == mb1:
        #         for j in range(db1, len(m[x])):
        #             m[x][j] += 1
        #     elif x == mb2 and mb1 != mb2:
        #         for j in range(db2+1):
        #             m[x][j] += 1
        #     else:
        #         for j in range(len(m[x])):
        #             m[x][j] += 1
        ans = 0
        for i in range(1, 13):
            for j in range(1, len(m[i])):
                if m[i][j] == 2:
                    ans += 1
        # print(m)
        return ans
