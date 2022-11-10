class Solution:
    def equalFrequency(self, word: str) -> bool:
        n = len(word)
        for i in range(n):
            mp = dict()
            for p in range(0, i):
                if word[p] in mp:
                    mp[word[p]] += 1
                else:
                    mp[word[p]] = 1
            for p in range(i + 1, n):
                if word[p] in mp:
                    mp[word[p]] += 1
                else:
                    mp[word[p]] = 1
            count = list()
            for a in mp:
                count.append(mp[a])
            c = len(set(count))
            if c == 1:
                return True
        return False

        #         n = len(word)
#         if n == 1:
#             return True
#         mp = dict()
#         for i in word:
#             if i in mp:
#                 mp[i] += 1
#             else:
#                 mp[i] = 1
#         count = list()
#         for a in mp:
#             count.append(mp[a])
#         print("mp:", mp)
#         c2 = set(count)
#         if len(c2) > 2:
#             return False

#         count.sort()
#         if count[len(count)-1] == count[len(count)-2]+1:
#             print("%%5")
#             return True
#         return False
#         # mp2 = dict()
#         # for i in count:
#         #     if i in mp2:
#         #         mp2[i] += 1
#         #     else:
#         #         mp2[i] = 1
