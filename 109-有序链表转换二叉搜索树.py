# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        def inorder(res, left, right) -> TreeNode:
            if left > right:
                return None
            mid = left + (right - left) // 2
            mid_root = TreeNode(res[mid])
            mid_root.left = inorder(res, left, mid-1)
            mid_root.right = inorder(res, mid+1, right)
            return mid_root
        root = inorder(res, 0, len(res)-1)
        return root