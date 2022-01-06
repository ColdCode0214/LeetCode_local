class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        l1, l2 = len(arr1), len(arr2)
        ans = 0
        flag = 0
        for i in range(l1):
            flag = 0
            for j in range(l2):
                if abs(arr1[i] - arr2[j]) <= d:
                    flag = 1
                    break
            if flag == 0:
                ans += 1
        return ans