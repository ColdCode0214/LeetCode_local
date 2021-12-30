# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def inorder(root, res):
            if root == None:
                return
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
        res = []
        inorder(root, res)
        res.sort()
        a = res[0]
        for i in range(len(res)):
            if res[i] > a:
                return res[i]
        return -1
