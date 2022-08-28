class Solution:
    def largestPalindromic(self, num: str) -> str:
        n = len(num)
        ans = ""
        count = dict()
        for i in range(n):
            if num[i] in count:
                count[num[i]] += 1
            else:
                count[num[i]] = 1

        def sortDict(data) -> dict:
            return dict(sorted(data.items(), key=operator.itemgetter(0), reverse=True))

        count = sortDict(count)
        # print(count)
        b, e, mid = "", "", ""
        for a in count:
            if count[a] % 2 == 0:
                if a != '0' or len(b) > 0:
                    b += a * int(count[a] / 2)
                    e = a * int(count[a] / 2) + e
            else:
                if a != '0' or len(b) > 0:
                    b += a * int((count[a] - 1) / 2)
                    e = a * int((count[a] - 1) / 2) + e
                if mid == "":
                    mid = a
        if len(b + mid + e) == 0 and "0" in count:
            return '0'

        return b + mid + e
