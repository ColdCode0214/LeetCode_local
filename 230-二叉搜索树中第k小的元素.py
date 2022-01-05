# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root, res):
            if not root:
                return
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
        res = []
        inorder(root, res)
        return res[k-1]