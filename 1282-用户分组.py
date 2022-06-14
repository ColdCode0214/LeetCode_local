class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        #groupSizes.sort()
        ans = list()
        mp = defaultdict(list)
        for i in range(n):
            mp[groupSizes[i]].append(i)
        #print(mp)
        ans = list()
        for k in mp:
            for i in range(0, len(mp[k]), k):
                temp = mp[k][i:i+k]
                ans.append(temp)
                # temp = list()
                # for j in range(k):
                #     temp.append(mp[k][j])
        return ans