"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.ans = list()
        def dfs(root):
            if root == None:
                return 
            self.ans.append(root.val)
            for ch in root.children:
                dfs(ch)
        dfs(root)
        return self.ans