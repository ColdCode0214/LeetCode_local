class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n = 0  # 记录num2中共有多少个1
        n2 = num2
        while num2 > 0:
            n += num2 % 2
            num2 = int(num2 / 2)
        # 求出num1哪些位置上有1
        n1 = list()
        cp1 = num1
        while num1 > 0:
            n1.insert(0, num1 % 2)
            num1 = int(num1 / 2)
        c1 = sum(n1)  # 求出num1中有多少个1
        lens = len(n1)
        ans = 0
        # print("n:", n)
        # print("c1:", c1)
        # print("n1:", n1)
        if c1 == n:
            return cp1
        elif c1 < n:
            diff = n - c1
            for i in range(lens - 1, -1, -1):
                if n1[i] == 0:
                    n1[i] = 1
                    diff -= 1
                if diff == 0:
                    break
            if diff > 0:
                t1 = [1] * diff
                t1.extend(n1)
            else:
                t1 = n1
            # print("n12:", n1)
            for i in range(len(t1)):
                if i < len(t1) - 1:
                    ans *= 2
                    ans += t1[i] * 2
                else:
                    ans += t1[i]
            # ans -= 1
        else:  # num1中1的数量大于num2中的c1>n
            # diff = c1 - n
            temp = list()
            for i in range(lens):
                if n1[i] == 1 and n > 0:
                    temp.append(1)
                    n -= 1
                else:
                    temp.append(0)
            # print("temp:", temp)
            for i in range(len(temp)):
                if i < len(temp) - 1:
                    ans *= 2
                    ans += temp[i] * 2
                else:
                    ans += temp[i]
            # ans -= 1
        return ans

