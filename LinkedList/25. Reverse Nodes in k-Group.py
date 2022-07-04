# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1

        return self.reverse(head, k, size)

    def reverse(self, head, k, size):
        if not head or size < k:
            return head

        prev, cur = None, head

        for i in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        head.next = self.reverse(cur, k, size - k)
        return prev



