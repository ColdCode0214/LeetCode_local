class Solution:
    def reformat(self, s: str) -> str:
        n = len(s)
        num_digit = 0
        letter, digit, ans = "", "", ""
        for i in range(n):
            if s[i].isdigit():
                digit += s[i]
            else:
                letter += s[i]
        if abs(len(digit) - len(letter)) > 1: return ""
        i1, i2 = 0, 0
        if len(letter) > len(digit):
            while i2 < len(digit):
                ans += letter[i1]
                ans += digit[i2]
                i1 += 1
                i2 += 1
            ans += letter[i1]
        else:
            while i1 < len(letter):
                ans += digit[i2]
                ans += letter[i1]
                i1 += 1
                i2 += 1
            if len(letter) != len(digit):
                ans += digit[i2]
        return ans

