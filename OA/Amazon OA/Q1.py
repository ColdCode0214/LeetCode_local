from typing import List

parcels = [4,2,3,4]

def q1(parcels: List[int]) -> int:
    n = len(parcels)
    ans = 0
    while sum(parcels) > 0:
        parcels.sort()
        pre = 0
        for i in range(n):
            if pre == 0 and parcels[i] != 0:
                pre = parcels[i]
            parcels[i] -= pre
        ans += 1
        print("par:", parcels)
    return ans

print(q1(parcels))
