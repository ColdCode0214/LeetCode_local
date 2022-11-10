class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            temp = list()
            if nums[i] % k == 0:
                if nums[i] == k:
                    ans += 1
                pre = nums[i]
                temp.append(nums[i])
                # print("temp1:", temp)
                for j in range(i + 1, n):
                    if nums[j] % k == 0:
                        temp.append(nums[j])
                        # print("bk1")
                        cur = min(pre, nums[j])
                        while cur != k:
                            flag = 0
                            for x in temp:
                                if x % cur != 0:
                                    flag = 1
                                    break
                            if flag == 1:
                                cur -= 1
                            else:
                                break
                        if cur == k:
                            ans += 1
                        # print("ans:", ans)
                        # # temp.append(nums[j])
                        # print("temp:", temp)
                    else:
                        break
        return ans



