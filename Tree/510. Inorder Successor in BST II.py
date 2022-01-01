"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # BST find first larger node.val

        # CASE1 --> check right nodes first (BST, right node value must < root.val)
        if node.right:
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur

            # CASE2 --> check root until root.val > node.val
        cur = node
        while cur.parent and cur.parent.val < node.val:
            cur = cur.parent

        return cur.parent




