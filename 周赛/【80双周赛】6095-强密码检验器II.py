class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)
        if n < 8: return False
        f1, f2, f3, f4 = 0, 0, 0, 0

        for i in range(n):
            if 97 <= ord(password[i]) <= 122:
                f1 = 1
            if 65 <= ord(password[i]) <= 90:
                f2 = 1
            if 48 <= ord(password[i]) <= 57:
                f3 = 1
            if password[i] in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]:
                f4 = 1
            if i != 0 and password[i] == password[i - 1]:
                return False
        if f1 == f2 == f3 == f4 == 1:
            return True
        else:
            return False