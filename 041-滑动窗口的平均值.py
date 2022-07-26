class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.nums = list()
        self.total = 0
        self.size = size



    def next(self, val: int) -> float:
        self.nums.append(val)
        self.total += val
        if self.size >= len(self.nums):
            ans = self.total/len(self.nums)
        else:
            self.total -= self.nums[0]
            self.nums.pop(0)
            ans = self.total/self.size
        return ans



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)