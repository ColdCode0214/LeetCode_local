# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        l, r = self.mirrorTree(root.left),self.mirrorTree(root.right)
        root.left, root.right = r, l
        return root