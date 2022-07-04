"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution1:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node

        prev, cur = head, head.next
        while prev.next != head:
            # Case1: 1 <- Node(2) <- 3
            if prev.val <= node.val <= cur.val:
                break

            # Case2: 3 -> 1, 3 -> Node(4) -> 1, 3 -> Node(0) -> 1
            if prev.val > cur.val and (node.val > prev.val or node.val < cur.val):
                break

            prev, cur = prev.next, cur.next

        node.next = cur
        prev.next = node
        return head




