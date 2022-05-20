"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # 复制原链表中的节点
        pre = head
        while pre != None:
            node = pre.next
            new = Node(pre.val)
            pre.next = new
            new.next = node
            pre = node

        # 复制random
        pre = head
        while pre != None:
            if pre.random:
                pre.next.random = pre.random.next
            pre = pre.next.next

        # 拆分两个链表并还原原始链表
        dummy = head.next
        pre = head.next
        while pre.next != None:
            pre.next = pre.next.next
            pre = pre.next
        return dummy