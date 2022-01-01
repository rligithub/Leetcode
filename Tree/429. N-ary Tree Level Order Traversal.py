"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # level traversal --> print path
        # BST
        if not root:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                cur = queue.popleft()
                level.append(cur.val)

                for child in cur.children:
                    queue.append(child)
            res.append(level)
        return res 