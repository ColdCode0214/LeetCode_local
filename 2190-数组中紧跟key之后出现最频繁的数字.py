class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freq = Counter()
        for i in range(1, len(nums)):
            if nums[i-1] == key:
                freq[nums[i]] += 1
        return freq.most_common(1)[0][0] #括号中的1表示找出现频率第1高的，后面的[0][0]表示取原数字而不是该数字出现的频率
        # most_common的返回值是 [(num1, times1), (num2, times2), (num3, times3)]