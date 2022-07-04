# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # quick sort
        # set two dummy head "small" and "large", and two moving pointers
        # put all smaller nodes in small linkedlist + all larger nodes in large linkedlist
        # merge two linkedlist

        dummySmall = ListNode(None)
        dummyLarge = ListNode(None)

        small, large = dummySmall, dummyLarge
        cur = head

        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next

            else:
                large.next = cur
                large = large.next
            cur = cur.next
        small.next = dummyLarge.next
        large.next = None

        return dummySmall.next
