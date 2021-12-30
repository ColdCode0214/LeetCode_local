# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def inorder(nums, left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = left + (right - left) // 2
            mid_root = TreeNode(nums[mid])
            mid_root.left = inorder(nums, left, mid - 1)
            mid_root.right = inorder(nums, mid + 1, right)
            return mid_root
        root = inorder(nums, 0, len(nums)-1)
        return root
