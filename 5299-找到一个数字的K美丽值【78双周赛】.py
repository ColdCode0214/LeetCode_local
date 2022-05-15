class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        lens = len(s)
        ans = 0
        for i in range(lens-k+1):
            a = ""
            for j in range(k):
                a += s[i+j]
            a = int(a)
            #print(a)
            if a != 0 and num%a == 0:
                ans += 1
        return ans