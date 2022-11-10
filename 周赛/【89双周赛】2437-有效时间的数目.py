class Solution:
    def countTime(self, time: str) -> int:
        h0, h1 = time[0], time[1]
        if h0 == '?' and h1 == '?':
            ans1 = 24
        elif h0 == '?':
            if int(h1) <= 3:
                ans1 = 3
            else:
                ans1 = 2
        elif h1 == '?':
            if int(h0) == 2:
                ans1 = 4
            else:
                ans1 = 10
        else:
            ans1 = 1
        m1, m2 = time[3], time[4]
        if m1 == '?' and m2 == '?':
            ans2 = 60
        elif m1 == '?':
            ans2 = 6
        elif m2 == '?':
            ans2 = 10
        else:
            ans2 = 1
        # print("ans1:", ans1, "ans2:", ans2)
        return ans1*ans2