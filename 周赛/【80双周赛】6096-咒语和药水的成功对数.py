class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        s, p = list(), list()
        mp = dict()
        for i in spells:
            s.append(i)
            mp[i] = -1
        for i in potions:
            p.append(i)
        s.sort(), p.sort()

        ans = list()
        temp = m - 1

        for i in range(n):
            if mp[s[i]] == -1:
                if temp == -1:
                    mp[s[i]] = m
                else:
                    while s[i] * p[temp] >= success:
                        if temp > 0:
                            temp -= 1
                        else:
                            temp = -1
                            break
                    mp[s[i]] = m - (temp + 1)

                # temp = 0

                # for j in range(m-1, -1, -1):
                #     if s[i] * p[j] >= success:
                #         temp += 1
                #     else:
                #         break
                # mp[s[i]] = temp
        for i in spells:
            ans.append(mp[i])
        return ans

