class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        for a in range(1, int(sqrt(num))+1):
            if num%a == 0:
                if a != num:
                    sum += a
                if int(num / a) != num  and int(num / a) != a:
                    sum += int(num / a)
        #print("sum:", sum)
        return sum == num