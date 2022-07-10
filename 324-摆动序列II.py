class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        # ans = list()
        n = len(nums)
        if n % 2 == 1:
            a, b = nums[0:int(n / 2) + 1], nums[int(n / 2) + 1:n]
        else:
            a, b = nums[0:int(n / 2)], nums[int(n / 2):n]
        a.reverse()
        b.reverse()
        nums.clear()
        for i in range(int(n / 2)):
            nums.append(a[i])
            nums.append(b[i])
        if n % 2 == 1:
            nums.append(a[len(a) - 1])
        return
