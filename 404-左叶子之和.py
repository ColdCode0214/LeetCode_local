# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def isLeaf(root: TreeNode) -> bool:
            return root.left == None and root.right == None

        def dfs(root: TreeNode) -> int:
            ans = 0
            if root.left:
                if isLeaf(root.left):
                    ans += root.left.val
                else:
                    ans += dfs(root.left)
            if root.right and not isLeaf(root.right):
                ans = ans + dfs(root.right)
            return ans

        return dfs(root) if root else 0