"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # similar to #116, but #116 is a perfect binary tree with two child nodes for all
        # this is regular binary tree, may only have one child node
        if not root:
            return

        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)

            for i in range(size):
                cur = queue.popleft()
                if queue:
                    cur.next = queue[0]
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            cur.next = None

        return root
