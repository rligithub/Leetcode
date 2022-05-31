# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not n or not head:
            return head

        dummyhead = ListNode(None)
        dummyhead.next = head

        slow, fast = dummyhead, dummyhead

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next  # only delete one node
        return dummyhead.next