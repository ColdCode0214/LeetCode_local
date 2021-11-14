# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        for i in range(int(len(arr)/2)):
            if arr[i]!=arr[len(arr)-1-i]:
                return False
        return True
