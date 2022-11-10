class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        mp = dict()
        for i in range(n):
            mp[heights[i]] = names[i]
        heights.sort()
        heights.reverse()
        ans = list()
        for i in range(n):
            ans.append(mp[heights[i]])
        return ans