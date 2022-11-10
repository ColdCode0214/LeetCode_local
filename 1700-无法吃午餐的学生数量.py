class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s1, s0 = sum(students), len(students) - sum(students)
        for i in range(len(sandwiches)):
            if sandwiches[i] == 0 and s0 > 0:
                s0 -= 1
            elif sandwiches[i] == 1 and s1 > 0:
                s1 -= 1
            else:
                break
        return s0 + s1