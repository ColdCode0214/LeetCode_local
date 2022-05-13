class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        pre = 0
        ans = list()
        for i in range(len(nums)):
            if i < len(nums)-1:
                if nums[i+1]>nums[i]+1:
                    if pre < i:
                        ans.append(str(nums[pre])+"->"+str(nums[i]))
                    else:
                        ans.append(str(nums[pre]))
                    pre = i+1
            else:
                if pre < i:
                    ans.append(str(nums[pre])+"->"+str(nums[i]))
                else:
                    ans.append(str(nums[pre]))
        return ans
