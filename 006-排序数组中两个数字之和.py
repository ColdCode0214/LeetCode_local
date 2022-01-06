class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lens = len(numbers)
        left, right = 0, lens-1
        #mid = (left + right) / 2
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [left, right]