# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:  # non-recurisive
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummyhead = ListNode(None)
        dummyhead.next = head

        prev, cur = dummyhead, head

        for i in range(left):
            prevFrozen = prev  # at node 1
            curFrozen = cur  # at node 2
            prev = prev.next  # at node 2
            cur = cur.next  # at node 3

        for i in range(right - left):
            nxt = cur.next
            cur.next = prev
            prev = cur  # at position node 4
            cur = nxt  # at position node 5

        prevFrozen.next = prev  # make 1 point to 4
        curFrozen.next = cur  # make 2 point to 5

        return dummyhead.next


