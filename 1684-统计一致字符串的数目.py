class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for a in words:
            flag = True
            for s in a:
                if s not in allowed:
                    flag = False
                    break
            if flag: ans += 1
        return ans

    # class Solution:
#     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#         res = 0
#         for word in words:
#             in_flag = True
#             for w in word:
#                 if w not in allowed:
#                     in_flag = False
#                     break
#             if in_flag:
#                 res += 1
#         return res
