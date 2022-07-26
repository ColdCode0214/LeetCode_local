class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        nums = list()
        for i in asteroids:
            flag = 0
            if i > 0: #当前元素为正数
                nums.append(i)
            else: #当前元素为负数
                if len(nums) == 0: #当前数组为空
                    nums.append(i)
                else: #当前数组不为空
                    if nums[len(nums)-1] < 0: #当前尾元素为负数
                        nums.append(i)
                    else: #当前尾元素为正数
                        if -i == nums[len(nums)-1]:
                            nums.pop()
                        elif -i > nums[len(nums)-1]:
                            nums.pop()
                            while len(nums) > 0:
                                if nums[len(nums)-1] < 0: 
                                    nums.append(i)
                                    break
                                elif -i > nums[len(nums)-1]: 
                                    nums.pop()
                                elif -i == nums[len(nums)-1]:
                                    nums.pop()
                                    flag = 1
                                    break
                                else:
                                    break
                            if flag == 0 and len(nums) == 0: nums.append(i)
        return nums


