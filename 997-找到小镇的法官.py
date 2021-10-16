class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people, judge = set(range(1,n+1)), defaultdict(int)
        for p, j in trust:
            if p in people:
                people.remove(p)
            judge[j]+=1
        if len(people) != 1:
            return -1
        person = people.pop()
        return -1 if judge.get(person, 0) != n-1 else person