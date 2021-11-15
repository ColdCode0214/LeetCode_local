# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans = []
        cur = head
        while cur:
            ans.insert(0, cur.val)
            cur = cur.next
        return ans