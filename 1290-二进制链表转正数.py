# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans=0
        cur = head
        while(cur):
            ans = ans * 2
            ans = ans + cur.val
            cur = cur.next
        return ans