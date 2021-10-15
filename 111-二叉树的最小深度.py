# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if not root.left and not root.right: #当没有子节点时只有一层“根节点”；仅有一方为空时不能直接算深度为1，因为题目定义是一定要找到叶子结点
            return 1
        mindepth = 10**9
        if root.left:
            mindepth = min(self.minDepth(root.left), mindepth)
        if root.right:
            mindepth = min(self.minDepth(root.right), mindepth)
        return mindepth+1
