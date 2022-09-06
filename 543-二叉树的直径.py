# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 1
        def dfs(root):
            # 访问到空节点时返回0
            if root == None: return 0
            # 求左右子树的深度
            L = dfs(root.left)
            R = dfs(root.right)
            # 计算dnode, 并更新ans
            self.ans = max(self.ans, L+R+1)
            # 返回以该节点为根的树的深度
            return max(L, R)+1
        dfs(root)
        return self.ans-1