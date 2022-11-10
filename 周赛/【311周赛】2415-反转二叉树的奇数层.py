# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        h = 0
        # def dfs(root, h):
        #     if root == None:
        #         return 0
        #     if h%2 == 0 and root.left != None and root.right != None:
        #         # print("&&")
        #     # if h%2 == 0:
        #         root.left.val, root.right.val = root.right.val, root.left.val
        #     dfs(root.left, h+1)
        #     dfs(root.right, h+1)
        # dfs(root, h)
        # return root
        stack = list()
        stack.append(root)
        while stack:
            n = len(stack)
            v = list()
            temp = list()
            for i in range(n):
                cur = stack.pop(0)
                if cur.left and cur.right:
                    stack.append(cur.left)
                    stack.append(cur.right)
                    if h % 2 == 0:
                        v.append(cur.left.val)
                        v.append(cur.right.val)
                        # if h%2 == 0:
                        temp.append(cur.left)
                        temp.append(cur.right)
            if h % 2 == 0:
                v.reverse()
                # print("len_v:", len(v), "len_t:", len(temp))
                for k in range(len(temp)):
                    temp[k].val = v[k]
            h += 1
        return root



