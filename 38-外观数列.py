class Solution:
    def countAndSay(self, n: int) -> str:
        count = 1
        s = "1"
        # if n == 1:
        #     return s
        ans = ""
        key, val = 0, 0
        while count < n:
            lens = len(s)
            for i in range(lens):
                if i == 0:
                    key = int(s[i])
                    val = 1
                else:
                    if s[i] == s[i-1]:
                        val += 1
                    else:
                        ans += str(val)
                        ans += str(key)
                        key = int(s[i])
                        val = 1
                if i == lens-1:
                    ans += str(val)
                    ans += str(key)
            s = ans
            ans = ""
            count += 1

        return s