class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp = {s:i for i, s in enumerate(list1)}
        ans = list()
        k = len(list1) + len(list2)

        for i in range(len(list2)):
            if list2[i] in mp.keys():
                if i+mp[list2[i]] < k:
                    ans.clear()
                    ans.append(list2[i])
                    k = i+mp[list2[i]]
                elif i+mp[list2[i]] == k:
                    ans.append(list2[i])
        return ans