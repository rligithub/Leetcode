"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution1:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return
        for child in root.children:
            self.dfs(child)

        self.res.append(root.val)


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        return [v for child in root.children for v in self.postorder(child)] + [root.val]


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return
        for child in root.children:
            self.dfs(child, res)

        return res.append(root.val)