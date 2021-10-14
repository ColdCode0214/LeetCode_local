# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        def check(rootLeft: TreeNode, rootRight: TreeNode):
            if not rootLeft and not rootRight:
                return True
            if not rootLeft or not rootRight:
                return False
            return (rootLeft.val == rootRight.val) and (check(rootLeft.left, rootRight.right)) and (
                check(rootLeft.right, rootRight.left))

        return check(root, root)
