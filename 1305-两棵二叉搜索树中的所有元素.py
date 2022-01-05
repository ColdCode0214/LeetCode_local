# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root, res):
            if not root:
                return
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)

        res1 = []
        inorder(root1, res1)
        res2 = []
        inorder(root2, res2)
        ans = []
        if len(res1) == 0 and len(res2) == 0:
            return ans
        if len(res1) == 0:
            return res2
        if len(res2) == 0:
            return res1

        p1 = 0
        p2 = 0

        while p1 < len(res1) and p2 < len(res2):
            if res1[p1] < res2[p2]:
                ans.append(res1[p1])
                p1 += 1
            else:
                ans.append(res2[p2])
                p2 += 1
        while p1 < len(res1):
            ans.append(res1[p1])
            p1 += 1
        while p2 < len(res2):
            ans.append(res2[p2])
            p2 += 1
        return ans