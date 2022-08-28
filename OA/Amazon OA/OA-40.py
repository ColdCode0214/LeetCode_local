from typing import List

packageWeights = [2,9,10,3,7]

def oa1t40(packageWeights: List[int]) -> int:
    n = len(packageWeights)
    l, r = n-2, n-1
    while l >= 0 and r >= 0:
        if packageWeights[l] < packageWeights[r]:
            packageWeights[r] += packageWeights[l]
            packageWeights[l] = -1
            l -= 1
        else:
            r = l
            l -= 1
    return max(packageWeights)

print(oa1t40(packageWeights))