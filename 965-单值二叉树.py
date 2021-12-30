# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        left_correct = ((not root.left) or (self.isUnivalTree(root.left) and root.left.val == root.val))
        right_correct = ((not root.right) or (self.isUnivalTree(root.right) and root.right.val == root.val))
        return left_correct and right_correct