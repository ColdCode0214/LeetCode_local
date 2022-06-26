class Solution:
    def greatestLetter(self, s: str) -> str:
        n = len(s)
        #s.sort()
        #print(s)
        ans = ""
        for i in range(n):
            if 65 <= ord(s[i]) <= 90:
                if s[i].lower() in s:
                    if ans == "":
                        ans = s[i]
                    else:
                        if ord(s[i]) > ord(ans):
                            ans = s[i]
        return ans