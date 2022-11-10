class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        nums = list()
        cp = n
        sum_ = 0
        while cp > 0:
            sum_ += cp%10
            cp = int(cp/10)
        if sum_ <= target:
            return 0
        count = 1
        while 1:
            cp = (int(n / pow(10, count)) + 1) * pow(10, count)
            # print("cp:", cp)
            sum_ = 0
            temp = cp
            while cp > 0:
                # nums.insert(0, cp%10)
                sum_ += cp%10
                cp = int(cp/10)
            if sum_ <= target:
                return temp - n
            count += 1
        # ans = 0
        # sum_ = sum(nums)
        # index = len(nums)-1
        # while sum_ > target:
        #     diff = 10 - nums[index]
        #     if diff != 10:
        #         ans += diff * pow(10, len(nums)-1-index)
        #         sum_ -= nums[index]
        #         sum_ +=