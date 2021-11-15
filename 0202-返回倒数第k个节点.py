# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        if not head:
            return head
        cur = head
        count = 0
        while cur:
            count = count + 1
            cur = cur.next
        cur = head
        for i in range(count - k):
            cur = cur.next
        return cur.val