class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        if n1 % 2 == 0 and n2 % 2 == 0:
            return 0
        res = 0
        if n1 % 2 == 0:
            for i in range(n1):
                res ^= nums1[i]

        elif n2 % 2 == 0:
            for i in range(n2):
                res ^= nums2[i]
        else:
            for i in range(n1):
                res ^= nums1[i]
            for i in range(n2):
                res ^= nums2[i]
        return res