# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val) and self.check(p.left, q.right) and self.check(p.right, q.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root)
