# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = 10000
        self.pre = -1

        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            if self.pre != -1:
                self.ans = min(self.ans, root.val - self.pre)
            self.pre = root.val
            dfs(root.right)

        dfs(root)
        return self.ans