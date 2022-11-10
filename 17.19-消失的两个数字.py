class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        sum_  = sum(nums)
        n = len(nums) + 2
        total = int((1+n)*n/2)
        sumTwo = total - sum_
        limit = sumTwo/2
        # print("limit:", limit)
        sum_ = 0
        for a in nums:
            if a <= limit:
                sum_ += a
        t2 = int((1+int(limit))*int(limit)/2)
        # print(sum_, t2)
        x = t2 - sum_
        return [x, sumTwo-x]