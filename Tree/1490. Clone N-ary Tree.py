"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        # copy value to hashmap
        # copy pointers
        if not root:
            return
        hashmap = {}
        self.dfs(root, hashmap)
        return hashmap[root]

    def dfs(self, root, hashmap):
        if not root:
            return

        hashmap[root] = Node(root.val)
        for child in root.children:
            hashmap[root].children.append(self.dfs(child, hashmap))

        return hashmap[root]