"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:  # DFS + find root FIRST
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # similar to #236, but each nodes has parent pointers, but not root
        # find a root first
        root = p
        while root.parent:
            root = root.parent

        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        if not root:
            return None

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if root == p or root == q:
            return root

        if left and right:
            return root

        if not left and not right:
            return None
        if left or right:
            return left or right


class Solution:  # while loop until ppp == qqq
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        ppp = p
        qqq = q

        while ppp != qqq:
            if ppp.parent:
                ppp = ppp.parent
            else:
                ppp = q
            if qqq.parent:
                qqq = qqq.parent
            else:
                qqq = p

        return ppp






