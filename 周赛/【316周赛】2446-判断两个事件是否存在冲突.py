class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def getTime(s) -> int:
            ans = list()
            ans = [int(x) for x in s.split(":")]
            m = ans[0]
            n = ans[1]
            res = m*100+n
            return res
        # s1, e1 = event1[0], event1[1]
        # s2, e2 = event2[0], event2[1]
        # def overlap(s1, e1, s2, e2) -> bool:
        #     if (s2 > s1 and s2 < e1) or (e2 > s1 and e2 < e1):
        #         return true
        #     elif s2 == s1:
        #         if
        s1, e1, s2, e2 = getTime(event1[0]), getTime(event1[1]), getTime(event2[0]), getTime(event2[1])
        # print(s1, e1, s2, e2)
        if s2 >= s1 and s2 <= e1:
            # print("1")
            return True
        if e2 >= s1 and e2 <= e1:
            # print("2")
            return True
        if s1 >= s2 and s1 <= e2:
            # print("3")
            return True
        if e1 >= s2 and e1 <= e2:
            # print("4")
            return True
        return False