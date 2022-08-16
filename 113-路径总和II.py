# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = list()
        path = list()
        cur = 0

        def dfs(root, cur):
            if root == None: return
            path.append(root.val)
            cur += root.val
            if root.left == None and root.right == None:
                if cur == targetSum:
                    ans.append(path[:])
            else:
                dfs(root.left, cur)
                dfs(root.right, cur)
            path.pop()

        # def dfs(root, targetSum):
        #     if root == None: return
        #     path.append(root.val)
        #     targetSum -= root.val
        #     if root.left == None and root.right == None:
        #         if targetSum == 0:
        #             ans.append(path[:])
        #     dfs(root.left, targetSum)
        #     dfs(root.right, targetSum)
        #     path.pop()
        dfs(root, cur)
        return ans