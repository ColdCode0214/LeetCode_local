class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        elif num < k:
            return -1
        elif num == k:
            return 1
        else:
            if k == 0:
                if num % 10 == 0:
                    return 1
                else:
                    return -1
            count = 1
            n2 = k
            while n2 < num:
                n2 = count * k
                if n2 % 10 == num % 10:
                    return count
                count += 1
            return -1
