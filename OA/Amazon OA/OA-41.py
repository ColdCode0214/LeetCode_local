import math
from collections import Counter
from typing import List

weights = [2,4,6,6,4,2,4]

def oa1t41(weights: List[int]) -> int:
    count = Counter(weights)
    ans = 0
    for a in count:
        if count[a] == 1: return -1
        ans += math.ceil(count[a]/3)
    return ans

print(oa1t41(weights))