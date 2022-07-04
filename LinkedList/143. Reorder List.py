# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
            # step1: find middle
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid, nxtmid = slow, slow.next
        mid.next = None  # disconnect mid

        # step2: reverse 2nd half
        prev, cur = None, nxtmid

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

            # prev -> head of 2nd half linkedlist

        # step3: merge two linkedlists
        while head and prev:
            next_head, next_prev = head.next, prev.next

            head.next = prev
            prev.next = next_head

            head, prev = next_head, next_prev

        return


