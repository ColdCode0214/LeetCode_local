class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr)%3 != 0: return False
        tar = int(sum(arr)/3)
        # print("tar:", tar)
        count, sum_ = 0, 0
        n = len(arr)
        for i in range(n):
            sum_ += arr[i]
            if sum_ == tar:
                count += 1
                sum_ = 0
            if count == 2:
                if i != n-1 and sum(arr[i+1:]) == tar:
                    return True
                else:
                    return False
        return False