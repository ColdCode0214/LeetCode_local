'''
Amazon OA-09
The team at Prime Video is developing a method to divide movies into groups based on the number
of awards thay have won.
A group can consist of any number of movies, but the difference in the number of awards won by
any two movies in the group must not exceed k.
The movies can be grouped together irrespective of their initial order.
Determine the minimum number of groups that can be formed such that each movie is in exactly one group.
'''
from typing import List

awards = [1,5,4,6,8,9,2]
k = 3

def oa1t9(awards: List[int], k: int) -> int:
    awards.sort()
    pre = awards[0]-k-1
    ans = 0
    for a in awards:
        if a - pre > k:
            ans += 1
            pre = a
    return ans+1

print(oa1t9(awards, k))