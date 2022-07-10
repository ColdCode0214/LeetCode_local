# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        top, bottom, left, right = 0, m - 1, 0, n - 1
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        i, j, temp = 0, 0, 0

        if not head: return ans
        cur = head

        while top <= bottom and left <= right:

            i = temp
            for j in range(left, right + 1):
                ans[i][j] = cur.val
                if not cur.next:
                    return ans
                cur = cur.next
                temp = j
            top += 1
            if top > bottom:
                break
            j = temp
            for i in range(top, bottom + 1):
                ans[i][j] = cur.val
                if not cur.next:
                    return ans
                cur = cur.next
                temp = i
            right -= 1
            if left > right:
                break
            i = temp
            for j in range(right, left - 1, -1):
                ans[i][j] = cur.val
                if not cur.next:
                    return ans
                cur = cur.next
                temp = j
            bottom -= 1
            if top > bottom:
                break
            j = temp
            for i in range(bottom, top - 1, -1):
                ans[i][j] = cur.val
                if not cur.next:
                    return ans
                cur = cur.next
                temp = i
            left += 1
            if left > right:
                break

            print("l,r,t,b:", left, right, top, bottom)

        return ans
