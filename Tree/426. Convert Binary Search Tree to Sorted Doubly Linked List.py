"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution1:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # in-order
        head, tail = self.dfs(root, None)
        return head

    def dfs(self, root, parent):
        head, tail = root, root

        if not root:
            return head, tail

        if root.left:
            headL, tailL = self.dfs(root.left, root)
            root.left = tailL
            tailL.right = root
            head = headL

        if root.right:
            headR, tailR = self.dfs(root.right, root)
            root.right = headR
            headR.left = root
            tail = tailR

        tail.right = head
        head.left = tail

        return head, tail


class Solution2:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # in-order
        if not root:
            return
        head, tail = self.dfs(root, None)
        tail.right = head
        head.left = tail
        return head

    def dfs(self, root, parent):
        head, tail = root, root

        if not root:
            return head, tail

        if root.left:
            headL, tailL = self.dfs(root.left, root)
            root.left = tailL
            tailL.right = root
            head = headL

        if root.right:
            headR, tailR = self.dfs(root.right, root)
            root.right = headR
            headR.left = root
            tail = tailR

        return head, tail


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.head = None
        self.prev = None

        self.dfs(root)

        self.prev.right = self.head
        self.head.left = self.prev

        return self.head

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)

        if self.prev:
            root.left = self.prev
            self.prev.right = root
        else:
            # Otherwise we are in the head position
            self.head = root
        self.prev = root

        self.dfs(root.right)