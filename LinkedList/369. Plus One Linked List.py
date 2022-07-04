# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # 一个整数 123 --> 每个digi代表一个node，要求在末尾上加上一个1，生成的新的linkedlist --> 有可能 99 --> 100
        c = self.getcarry(head)
        if c == 0:
            return head
        else:
            newhead = ListNode(c)
            newhead.next = head
            return newhead

    def getcarry(self, node):
        if not node:
            return 1  # last node plus 1

        c = self.getcarry(node.next)
        node.val += c
        c = 0
        if node.val == 10:
            c = 1
            node.val = 0
        return c