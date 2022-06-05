# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode()
        dummy = pre
        carry = 0
        cur1, cur2 = l1, l2
        while cur1 and cur2:
            ans = ListNode()
            pre.next = ans
            ans.val = cur1.val + cur2.val + carry
            if ans.val >= 10:
                ans.val -= 10
                carry = 1
            else:
                carry = 0
            pre = ans
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            ans = ListNode()
            pre.next = ans
            ans.val = cur1.val + carry
            if ans.val >= 10:
                ans.val -= 10
                carry = 1
            else:
                carry = 0
            pre = ans
            cur1 = cur1.next
        while cur2:
            ans = ListNode()
            pre.next = ans
            ans.val = cur2.val + carry
            if ans.val >= 10:
                ans.val -= 10
                carry = 1
            else:
                carry = 0
            pre = ans
            cur2 = cur2.next
        if carry == 1:
            ans = ListNode()
            pre.next = ans
            ans.val = 1
        return dummy.next