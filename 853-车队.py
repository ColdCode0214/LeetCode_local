class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        mp = dict()
        for i in range(n):
            mp[position[i]] = (target-position[i])/speed[i]
        def dictSort(data) -> dict:
            return dict(sorted(data.items(), key = operator.itemgetter(0), reverse = False))
        mp = dictSort(mp)
        # print(mp)
        stack = list()
        for a in mp.keys():
            while stack and mp[stack[len(stack)-1]] <= mp[a]:
                stack.pop()
            stack.append(a)
        return len(stack)