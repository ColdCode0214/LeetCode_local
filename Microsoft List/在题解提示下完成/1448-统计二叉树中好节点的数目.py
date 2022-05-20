# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, mymax):
            nonlocal ans
            if root == None:
                return
            if root.val >= mymax:
                ans += 1
                mymax = root.val
            dfs(root.left, mymax)
            dfs(root.right, mymax)
        dfs(root, root.val)
        return ans