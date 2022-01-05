# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        node = root
        res = None
        while node is not None:
            if node.val > p.val:
                res = node
                node = node.left
            else:
                node = node.right
        return res
        
