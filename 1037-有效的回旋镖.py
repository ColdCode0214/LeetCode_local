class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        if points[1][0] != points[0][0]:
            k1 = (points[1][1]-points[0][1]) / (points[1][0]-points[0][0])
        else:
            if points[1][0] == points[2][0]:
                return False
            else:
                k1 = 999999
        if points[2][0] != points[1][0]:
            k2 = (points[2][1]-points[1][1]) / (points[2][0]-points[1][0])
        else:
            if points[1][0] == points[0][0]:
                return False
            else:
                k2 = 999999
        return k1 != k2