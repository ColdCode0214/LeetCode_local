class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = list()
        ans1 = list()
        ans2 = list()
        #list1 = {s:i for i,s in enumerate(nums1)}
        for a in nums1:
            if a not in nums2:
                ans1.append(a)
        for a in nums2:
            if a not in nums1:
                ans2.append(a)
        ans1 = list(set(ans1))
        ans2 = list(set(ans2))
        ans.append(ans1)
        ans.append(ans2)
        return ans