class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        temp = sorted(list(zip(nums, cost)))
        total, note = sum(cost), 0
        for num, count in temp:
            note += count
            if note > total // 2:
                target = num
                break
        ans = 0
        print("target:", target)
        for num, count in temp:
            ans += abs(target-num) * count
        return ans



# class Solution:
#     def minCost(self, nums: List[int], cost: List[int]) -> int:
#         tmp = sorted(zip(nums, cost))
#         tot, note = sum(cost), 0
#         for num, c in tmp:
#             note += c
#             if note > tot // 2:
#                 chosen = num
#                 break
#         print("chosen:", chosen)
#         return sum(c * abs(num - chosen) for num, c in tmp)