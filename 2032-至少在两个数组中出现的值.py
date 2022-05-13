class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # t1 = {s:i for i,s in enumerate(nums1)}
        # t2 = {s:i for i,s in enumerate(nums2)}
        ans = list()
        for a in nums1:
            if a in nums2 or a in nums3:
                ans.append(a)
        for a in nums2:
            if a in nums1 or a in nums3:
                ans.append(a)
        for a in nums3:
            if a in nums1 or a in nums2:
                ans.append(a)
        return list(set(ans))