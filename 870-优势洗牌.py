class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        ans = list()
        n = len(nums2)
        for a in nums2:
            if a >= nums1[len(nums1)-1] or a < nums1[0]:
                ans.append(nums1[0])
                nums1.pop(0)
            else:
                l, r = 0, len(nums1)-1
                while l != r:
                    mid = (l+r) // 2
                    if nums1[mid] > a:
                        r = mid
                    else:
                        l = mid + 1
                ans.append(nums1[l])
                nums1.pop(l)
        return ans
