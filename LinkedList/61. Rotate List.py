# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

            # step1: check the size of linkedlist and make oldTail connect to oldHead
        dummy = head
        size = 1
        while dummy.next:
            dummy = dummy.next
            size += 1
        dummy.next = head

        # step2: find newtail and new head --> n - k - 1
        k = k % size
        newTail = head
        for i in range(size - k - 1):
            newTail = newTail.next
        newHead = newTail.next

        newTail.next = None

        return newHead

