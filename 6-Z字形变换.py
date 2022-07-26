class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows <= 1:
            return s
        zz = ['' for _ in range(numRows)]
        row = 0
        flag = -1
        for a in s:
            print("row:", row)
            zz[row] += a
            if row == numRows-1 or row == 0: flag = -flag
            row += flag
        return "".join(zz)
