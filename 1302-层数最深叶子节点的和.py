# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans, max_ = 0, -1
        def dfs(root, height):
            if root == None:
                return
            nonlocal ans, max_ # 需要修改函数外的变量时加上nonlocal关键字
            if root.left == None and root.right == None:
                if height > max_:
                    max_, ans = height, root.val
                elif height == max_:
                    ans += root.val
            else:
                dfs(root.left, height+1)
                dfs(root.right, height+1)
        dfs(root, 0)
        return ans