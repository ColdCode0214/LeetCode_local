class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        ans.append([])
        n = len(nums)
        for i in range(n):
            m = len(ans)
            for j in range(m):
                temp = copy.deepcopy(ans[j])
                temp.append(nums[i])
                temp.sort()
                if temp not in ans:
                    ans.append(temp)
        return ans