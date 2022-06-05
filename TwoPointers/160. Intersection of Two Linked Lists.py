# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        curA, curB = headA, headB

        while curA != curB:
            curA = curA.next
            curB = curB.next

            if curA and not curB:
                curB = headA

            if curB and not curA:
                curA = headB

        return curA