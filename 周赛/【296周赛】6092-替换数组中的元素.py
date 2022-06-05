class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        n = len(nums)
        m = len(operations)
        # for i in range(m):
        #     for j in range(n):
        #         if nums[j] == operations[i][0]:
        #             nums[j] = operations[i][1]
        #             break
        # return nums
        mp = {s: i for i, s in enumerate(nums)}
        for i in range(m):
            nums[mp[operations[i][0]]] = operations[i][1]
            # if operations[i][1] not in mp:
            mp[operations[i][1]] = mp[operations[i][0]]
            # else:

            mp[operations[i][0]] = -1
        return nums

