from typing import List

location = [1,7,6,8]
moveFrom = [1,7,2]
moveTo = [2,9,5]

def oa1t4(location: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
    times = len(moveTo)
    mp = dict()
    n = len(location)
    for i in range(n):
        mp[location[i]] = i
    for i in range(times):
        mp[moveTo[i]] = mp[moveFrom[i]]
        mp[moveFrom[i]] = -1
    ans = list()
    for a in mp:
        if mp[a] != -1:
            ans.append(a)
    ans.sort()
    return ans

print(oa1t4(location, moveFrom, moveTo))