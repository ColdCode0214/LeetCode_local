# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root, res):
            if root == None:
                return
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)
        res = []
        inorder(root, res)
        left = 0
        right = len(res)-1
        while left < right:
            if res[left] + res[right] == k:
                return True
            elif res[left] + res[right] > k:
                right -= 1
            else:
                left += 1
        return False
