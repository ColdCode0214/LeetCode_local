class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        n = len(s)
        n2 = len(sub)
        mp = defaultdict(set)
        #print(mp)
        n3 = len(mappings)
        # for i in range(n3):
        #     if mappings[i][0] in mp.keys():
        #         mp[mappings[i][0]].append(mappings[i][1])
        #     else:
        #         mp[mappings[i][0]] = [mappings[i][1]]
        for a,b in mappings:
            mp[a].add(b)
        for i in range(n-n2+1):
            temp = s[i:i+n2]
            for j in range(n2):
                if sub[j] != temp[j] and temp[j] not in mp[sub[j]]:
                    break
            else:
                return True

                #下面这种写法会超时
                # if temp[j] != sub[j]:

                #     if sub[j] not in mp.keys():
                #         i = j
                #         break
                #     else:

                #         if temp[j] not in mp[sub[j]]:
                #             i = j
                #             break
                #         else:
                #             if j == n2-1:
                #                 return True
                # else:
                #     if j == n2-1:
                #         return True

        return False
