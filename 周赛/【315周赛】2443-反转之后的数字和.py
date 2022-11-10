class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num+1):
            temp = str(i)
            temp = temp[::-1]
            cur = int(temp)
            if cur + i == num:
                return True
        return False