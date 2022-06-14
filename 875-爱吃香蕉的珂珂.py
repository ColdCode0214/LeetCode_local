class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n == h:
            return max(piles)
        piles.sort()
        div = h - n
        if div >= n:
            a = 1
        else:
            a = piles[n-1-div]
        b = ceil(piles[n-1]/2)
        #print("b:", b)
        l, r = a, b
        ans = 0
        while l <= r:
            #print("l:", l, "r:", r)
            ans = ceil((l+r)/2)
            #print("ans:", ans)
            sum = 0
            for i in range(n):
                sum += ceil(piles[i]/ans)
            if sum > h:
                l = ans + 1
            else:
                temp = 0
                if ans == 1:
                    return ans
                else:
                    for i in range(n):
                        temp += ceil(piles[i]/(ans-1))
                    if temp > h:
                        return ans
                    else:
                        r = ans - 1
        return l



