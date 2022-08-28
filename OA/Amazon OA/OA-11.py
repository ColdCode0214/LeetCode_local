from typing import List

tempChange = [-1,2,3]

def oa1t11(tempChange: List[int]) -> int:
    n = len(tempChange)
    ans = tempChange[0]
    sumbegin, sumend = 0, 0
    for i in range(n):
        sumbegin += tempChange[i]
        sumend += tempChange[n-1-i]
        temp = max(sumbegin, sumend)
        ans = max(temp, ans)
    return ans

print(oa1t11(tempChange))