class Solution: # 计数
    def minDeletions(self, s: str) -> int:
        # 统计小写英文字母出现的次数
        p = [s.count(chr(97 + i)) for i in range(26)]
        # 大到小排序
        p.sort(reverse=True)
        ans = 0
        for i in range(1, 26):
            # 上一个次数为0时，说明频次已经用完了
            if p[i - 1] == 0:
                # 把当前到后面的次数都应该降为0，所以都加上
                ans += sum(p[i:])
                break
            # 当出现当前次数>=上一个次数时，加上之间的落差 + 1,
            # 当前次数比上一个次数小1
            elif p[i] >= p[i - 1]:
                ans += p[i] - p[i - 1] + 1
                p[i] = p[i - 1] - 1
        return ans

