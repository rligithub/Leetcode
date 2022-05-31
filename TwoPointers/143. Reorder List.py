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
        # step1: find the middle node of the linked list
        # step2: reverse the 2nd half
        # step3: merge two linked list into one long linked list

        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(slow.val)

        mid, mid_next = slow, slow.next
        mid.next = None

        cur, prev = mid_next, None
        while cur:
            next_node = cur.next
            cur.next = prev

            prev = cur
            cur = next_node

        while head and prev:
            head_next, prev_next = head.next, prev.next

            head.next = prev
            prev.next = head_next

            head, prev = head_next, prev_next

        return 