# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root) -> bool:
            if root.left == None and root.right == None: 
                if root.val == 1: return True
                else: return False
            else:
                if root.val == 2:
                    #return evaluateTree(root.left) or evaluateTree(root.right)
                    if dfs(root.left) == True or dfs(root.right) == True: return True
                    else: return False
                    #return dfs(root.left) or dfs(root.right)
                else:
                    #return evaluateTree(root.left) and evaluateTree(root.right)
                    #return dfs(root.left) and dfs(root.right)
                    if dfs(root.left) == True and dfs(root.right) == True: return True
                    else: return False
        return dfs(root)