# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def construce_path(root, path):
            if root:
                path = path + str(root.val)
                #如果当前节点是叶子结点，则直接把当前路径加入路径集合中
                if root.left == None and root.right == None:
                    paths.append(path)
                else:
                    path = path + "->"
                    construce_path(root.left, path)
                    construce_path(root.right, path)
            return paths
        paths = []
        construce_path(root, '')
        return paths