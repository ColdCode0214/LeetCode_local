class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        temp = sum
        #print("sum:", sum)
        for i in range(1, len(nums)-k+1):
            temp = temp - nums[i-1] + nums[i+k-1]
            sum = max(sum, temp)
        return sum/k
