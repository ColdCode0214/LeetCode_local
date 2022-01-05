# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root:
            return None
        pre = None
        while root.val != p.val:
            if root.val < p.val:
                root = root.right
            else:
                pre = root
                root = root.left
        if root.right == None:
            return pre
        else:
            root = root.right
            while root.left:
                root = root.left
            return root