class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)
        ans = 0
        cp = list()
        for i in range(n):
            if s[i] == '0':
                cp.append(0)
            else:
                cp.append(1)
        flag = 0
        for i in range(n-1):
                if cp[i] == 0 and cp[i+1] == 1:
                    flag = 1
                    # ans = 1
                    break
        while flag == 1:
            index = 0
            flag = 0
            while index < n-1:
                if cp[index] == 0 and cp[index+1] == 1:
                    cp[index], cp[index+1] = 1, 0
                    index += 2
                else:
                    index += 1
            for i in range(n-1):
                if cp[i] == 0 and cp[i+1] == 1:
                    flag = 1
                    break
            ans += 1
        return ans
