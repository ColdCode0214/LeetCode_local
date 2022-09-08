class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        words = list()
        count = 0
        temp = ''
        for i in range(n):
            if text[i] == ' ':
                count += 1
                if len(temp) > 0:
                    words.append(temp)
                    temp = ''
            else:
                temp += text[i]
        if len(temp) > 0:
            words.append(temp)
        # print("count:", count)
        if count == 0:
            return text
        lens = len(words)
        if lens == 1:
            return words[0]+" "*count
        # print("lens:", lens)
        re = count%(lens-1)
        ea = count//(lens-1)
        ans = ''
        for i in range(lens):
            ans += words[i]
            if i < lens-1:
                ans += ' '*ea
            else: ans += " "*re
        return ans