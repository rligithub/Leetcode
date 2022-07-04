# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head
        prev, cur = dummy, head
        while cur and cur.next:
            if prev.next.val != cur.next.val:
                prev, cur = cur, cur.next
            else:
                while cur.next and prev.next.val == cur.next.val:
                    cur = cur.next
                prev.next, cur = cur.next, cur.next
        return dummy.next

