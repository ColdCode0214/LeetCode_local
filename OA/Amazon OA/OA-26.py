from typing import List

wheel = [4,5,6]

def oa1t26(wheel: List[int]) -> List[int]:
    res = list()
    n = len(wheel)
    for a in wheel:
        if a%2 == 1:
            res.append(0)
        else:
            res.append(int(a/4)+1)
    return res

print(oa1t26(wheel))