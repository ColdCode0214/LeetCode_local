# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        cur = 0
        def dfs(root, cur):
            if root == None: return
            cur *= 10
            cur += root.val
            if root.left == None and root.right == None:
                nonlocal ans
                ans += cur
            else:
                dfs(root.left, cur)
                dfs(root.right, cur)
        dfs(root, cur)
        return ans
