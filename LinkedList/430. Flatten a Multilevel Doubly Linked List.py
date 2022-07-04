"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution2:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        dummy = Node(None, None, head, None)
        self.dfs(dummy, head)
        dummy.next.prev = None
        return dummy.next

    def dfs(self, prev, cur):
        if not cur:
            return prev

        cur.prev = prev
        prev.next = cur

        nxtnode = cur.next
        tail = self.dfs(cur, cur.child)
        cur.child = None
        return self.dfs(tail, nxtnode)


class Solution1:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        self.dfs(head)
        return head

    def dfs(self, node):
        child = node.child
        nxt = node.next
        node.child = None

        if child and nxt:
            childEnd = self.dfs(child)
            nextEnd = self.dfs(nxt)

            node.next = child
            child.prev = node

            childEnd.next = nxt
            nxt.prev = childEnd
            return nextEnd

        elif not child and nxt:
            nextEnd = self.dfs(nxt)
            return nextEnd

        elif child and not nxt:
            childEnd = self.dfs(child)
            node.next = child
            child.prev = node
            return childEnd
        else:
            return node


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            if cur.child:
                right = cur.next
                cur.next = self.flatten(cur.child)
                # whoever is the next, set the prev as the current node, recursion will find the node.next
                cur.next.prev = cur
                cur.child = None
                # current node will keep going to all the way end then we connect the last layer
                while cur.next:
                    cur = cur.next
                # connect to last layer
                if right:
                    cur.next = right
                    right.prev = cur
            cur = cur.next
        return head