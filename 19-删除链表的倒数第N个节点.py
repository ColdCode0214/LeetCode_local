# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        f = head
        s = dummy
        for i in range(n):
            f = f.next
        while f:
            s = s.next
            f = f.next
        s.next = s.next.next
        return dummy.next #因为有可能删除的就是head，所以不能直接返回head