class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = list()
        end = list()
        for i in range(len(nums)):
            if i == 0:
                front.append(nums[i])
                end.append(nums[len(nums)-1-i])
            else:
                front.append(front[len(front)-1]*nums[i])
                end.append(end[len(end)-1]*nums[len(nums)-1-i])
        ans = list()
        for i in range(len(nums)):
            if i == 0:
                ans.append(end[len(nums)-2])
            elif i == len(nums)-1:
                ans.append(front[len(nums)-2])
            else:
                ans.append(front[i-1]*end[len(nums)-3-(i-1)])
        return ans