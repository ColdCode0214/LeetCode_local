# 使用次数多的字母尽量往前放
from typing import List
from collections import Counter
import operator

text = "abacadefghibj"

def oa1t2(text:str) -> int:
    count = Counter(text)
    miss = "abcdefghijklmnopqrstuvwxyz"
    for a in miss:
        if a not in count.keys(): count[a] = 0
    #print("count:", count)
    def dictSort(data) -> dict:
        return dict(sorted(data.items(), key = operator.itemgetter(1), reverse = True))
    count = dictSort(count)

    index = 0
    board = ["" for _ in range(9)]
    ans = 0
    temp = 1
    #print("count:", count)
    for a in count.keys():
        board[index] += a
        ans += temp * count[a]
        index += 1
        if index == 9:
            index = 0
            temp += 1
    return ans

print(oa1t2(text))
