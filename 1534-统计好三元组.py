class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        lens = len(arr)
        ans = 0
        for i in range(lens-2):
            for j in range(i+1, lens-1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, lens):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            ans+=1
        return ans