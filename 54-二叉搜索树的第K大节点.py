# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def inorder(root, res):
            if root == None:
                return
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)

        res = []
        inorder(root, res)
        temp = res[len(res) - 1]
        count = 1
        for i in range(len(res) - 1, -1, -1):
            if count == k:
                return temp
            if res[i] < temp:
                count += 1
                temp = res[i]

        return temp